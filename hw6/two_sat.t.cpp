#include "two_sat.h"

#include <gtest/gtest.h>
#include <algorithm>

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

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

