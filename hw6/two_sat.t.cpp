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

TEST(Randomize, NotAllFalse)
{
    std::vector<bool> vars(100);
    TwoSat::randomflip(vars);
    EXPECT_NE(vars.end(), std::find(vars.begin(), vars.end(), true));
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
    addConstraint(cv, -1, -2);
    EXPECT_FALSE(TwoSat::satisfiable(cv));
}

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

