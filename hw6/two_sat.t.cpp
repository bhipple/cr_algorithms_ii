#include "two_sat.h"

#include <gtest/gtest.h>
#include <algorithm>

void addConstraint(std::vector<TwoSat::Constraint>& cv, int x, int y) {
    TwoSat::Constraint c;
    c.x = x;
    c.y = y;
    cv.push_back(c);
}

TEST(LoadFile, Gets100kRecords)
{
    std::vector<TwoSat::Constraint> c = TwoSat::loadFile("../instances/2sat1.txt");
    EXPECT_EQ(100000, c.size());
}

TEST(Randomize, MixOfBoth)
{
    std::vector<bool> vars(100);
    TwoSat::randomflip(vars);
    EXPECT_NE(vars.end(), std::find(vars.begin(), vars.end(), true));
    EXPECT_NE(vars.end(), std::find(vars.begin(), vars.end(), false));
}

TEST(Satisfied, Yes)
{
    std::vector<bool> vars(3);
    vars[2] = true;
    TwoSat::Constraint c;
    c.x = -1;
    c.y = 2;
    EXPECT_TRUE(TwoSat::satisfied(c, vars));
}

TEST(Satisfied, No)
{
    std::vector<bool> vars(3);
    vars[1] = true;
    vars[2] = true;
    TwoSat::Constraint c;
    c.x = -1;
    c.y = -2;
    EXPECT_FALSE(TwoSat::satisfied(c, vars));
}

TEST(Unit, SmallSatisfiable)
{
    std::vector<TwoSat::Constraint> cv;
    addConstraint(cv, 1, 2);
    addConstraint(cv, -1, 2);
    ASSERT_TRUE(TwoSat::satisfiable(cv));
}

TEST(Unit, SmallUnsatisfiable)
{
    std::vector<TwoSat::Constraint> cv;
    addConstraint(cv, 1, 2);
    addConstraint(cv, 1, -2);
    addConstraint(cv, -1, 2);
    addConstraint(cv, -1, -2);
    EXPECT_FALSE(TwoSat::satisfiable(cv));
}

TEST(HW, FirstProblem)
{
    EXPECT_FALSE(TwoSat::satisfiable("../instances/2sat1.txt"));
}

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

