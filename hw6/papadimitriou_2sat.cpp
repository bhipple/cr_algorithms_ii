#include "papadimitriou_2sat.h"

#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <math.h>
#include <sstream>
#include <string>
#include <utility>
#include <algorithm>
#include <map>

namespace TwoSat {

std::vector<Constraint> loadFile(std::string fileName) {
    std::vector<Constraint> constraints;

    std::ifstream myfile;  // Uses RAII automatically!
    myfile.open(fileName);
    if(myfile.is_open()) {
        int x, y;
        std::string line;
        getline(myfile, line);  // Ignore the header
        while(getline(myfile, line)) {
            std::stringstream ss(line);
            ss >> x >> y;
            Constraint c;
            c.x = x;
            c.y = y;
            constraints.push_back(c);
        }
    }

    return constraints;
}

bool satisfied(const Constraint& c, const std::vector<bool>& cv)
{
    bool a = (c.x >= 0 ? cv[c.x] : !cv[abs(c.x)]);
    return a || (c.y >= 0 ? cv[c.y] : !cv[abs(c.y)]);
}

void randomflip(std::vector<bool>& vars)
{
    int r;
    for(auto var : vars) {
        r = rand() % 2;
        var = r;
    }
}

// Helper to see if we've detected both the positive and negative for a given variable #
struct Var {
    Var() {
        positive = false;
        negative = false;
    }
    bool positive;
    bool negative;
};

void setValCond(std::map<int,Var>& valConditions, int var)
{
    if(var < 0) {
        valConditions[-1*var].negative = true;
    } else {
        valConditions[var].positive = true;
    }
}

void preprocess(std::vector<Constraint>& cv, size_t varCt)
{
    size_t initialSize = cv.size();
    std::map<int, Var> valConditions;
    for(size_t i = 1; i <= varCt; ++i) {
        valConditions[i] = Var();
    }
    for(auto c : cv) {
        setValCond(valConditions, c.x);
        setValCond(valConditions, c.y);
    }
    for(int i = 1; i < static_cast<int>(valConditions.size()); ++i) {
        if(valConditions[i].positive != valConditions[i].negative) {
            cv.erase(std::remove_if(cv.begin(),
                                    cv.end(),
                                    [&](Constraint c){return abs(c.x) == i || abs(c.y) == i;}),
                     cv.end());
        }
    }
    std::cout << "Preprocessing removed " << initialSize - cv.size() << " conditions (" << cv.size() << " remain)." << std::endl;
    if(initialSize != cv.size()) { preprocess(cv, varCt); }
}

bool satisfiable(const std::string& fileName)
{
    std::vector<Constraint> cv = loadFile(fileName);
    return satisfiable(cv);
}

bool satisfiable(std::vector<Constraint>& cv)
{
    const size_t n = cv.size();
    preprocess(cv, n);

    std::vector<bool> vars(n+2);
    const size_t runs = log2(n) + 1;
    for(size_t i = 0; i <= runs; ++i) {
        std::cout << "Run " << i << " of " << runs << std::endl;
        randomflip(vars);
        for(size_t j = 0; j < 2*n*n; ++j) {
            std::vector<int> unsatisfied;
            for(size_t chk = 0; chk < cv.size(); ++chk) {
                if(!satisfied(cv[chk], vars)) {
                    unsatisfied.push_back(chk);
                }
            }
            if(unsatisfied.empty()) { return true; }

            int randConstraintIdx = rand() % unsatisfied.size();
            const Constraint& constr = cv[randConstraintIdx];
            if(rand() % 2) {
                vars[abs(constr.x)] = !vars[abs(constr.x)];
            } else {
                vars[abs(constr.y)] = !vars[abs(constr.y)];
            }
        }
    }
    return false;
}

}
