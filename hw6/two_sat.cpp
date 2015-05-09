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

void randomflip(std::vector<bool>& vars)
{
    int r;
    for(auto var : vars) {
        r = rand() % 2;
        var = r;
    }
}

bool satisfiable(const std::vector<Constraint>& constraints)
{
    const size_t n = constraints.size();

    std::vector<bool> vars(n);
    for(size_t i = 0; i <= log2(n); ++i) {
        randomflip(vars);
    }
    return false;
}

}
