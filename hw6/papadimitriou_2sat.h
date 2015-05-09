#ifndef INCLUDED_PAPADIMITRIOU_2SAT
#define INCLUDED_PAPADIMITRIOU_2SAT

#include <vector>
#include <string>

namespace TwoSat {

class Constraint {
  public:
    int x;
    int y;
};

bool satisfiable(const std::string& fileName);

bool satisfiable(std::vector<Constraint>& cv);
bool satisfied(const Constraint& c, const std::vector<bool>& cv);
void randomflip(std::vector<bool>& vars);

std::vector<Constraint> loadFile(std::string fileName);
void preprocess(std::vector<Constraint>& cv, size_t varCt);
}
#endif
