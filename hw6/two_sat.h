#ifndef INCLUDED_2SAT
#define INCLUDED_2SAT

#include <vector>
#include <string>

namespace TwoSat {

class Constraint {
  public:
    int x;
    int y;
};

bool satisfiable(const std::string& fileName);
bool satisfiable(const std::vector<Constraint>& cv);
bool satisfied(const Constraint& c, const std::vector<bool>& cv);

void prune(std::vector<Constraint>& cv);

std::vector<Constraint> loadFile(std::string fileName);
void randomflip(std::vector<bool>& vars);

}
#endif
