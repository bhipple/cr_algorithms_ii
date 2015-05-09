#ifndef INCLUDED_2SAT
#define INCLUDED_2SAT

#include <vector>
#include <string>

namespace TwoSat {

struct Constraint {
    int x;
    int y;
};

std::vector<Constraint> loadFile(std::string fileName);
void randomflip(std::vector<bool>& vars);
bool satisfiable(const std::vector<Constraint>& constraints);

}
#endif
