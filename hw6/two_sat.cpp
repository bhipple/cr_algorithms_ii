#include "two_sat.h"

#include <fstream>
#include <iostream>
#include <math.h>
#include <sstream>
#include <string>
#include <utility>
#include <cstdlib>

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
    bool a = (c.x >= 0 ? cv[c.x] : !cv[c.x]);
    return a || (c.y >= 0 ? cv[c.y] : !cv[c.y]);
}

void randomflip(std::vector<bool>& vars)
{
    int r;
    for(auto var : vars) {
        r = rand() % 2;
        var = r;
    }
}

bool satisfiable(const std::vector<Constraint>& cv)
{
    const size_t n = cv.size();

    std::vector<bool> vars(n+2);
    for(size_t i = 0; i <= log2(n); ++i) {
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
