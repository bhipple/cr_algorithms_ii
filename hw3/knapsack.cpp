#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

typedef std::vector<std::pair<size_t, size_t>> ItemVec;
typedef std::vector<std::vector<int>> DP;

ItemVec getItems(size_t& size, std::string fileName) {
    ItemVec items;

    std::ifstream myfile;  // Uses RAII automatically!
    myfile.open(fileName);
    if(myfile.is_open()) {
        std::string line, value, weight;
        getline(myfile, line);
        std::stringstream header(line);
        header >> size;
        while(getline(myfile, line)) {
            std::stringstream ss(line);
            ss >> value >> weight;
            std::pair<int, int> item = std::make_pair(std::stoi(value), std::stoi(weight));
            items.push_back(item);
        }
    }

    return items;
}

int calculateDecision(const DP& A, const ItemVec& items, size_t i, size_t x) {
    int skipThis = 0;
    int useThis = 0;
    if(i > 0) {
        skipThis = A[i-1][x];
    }

    int remainder = static_cast<int>(x) - static_cast<int>(items[i].second);
    if(remainder >= 0) {
        useThis = items[i].first;
        if(i > 0) {
            useThis += A[i-1][remainder];
        }
    }

    return std::max(skipThis, useThis);
}

int knapsack(size_t size, const ItemVec& items) {
    DP A;
    for(size_t i = 0; i < items.size(); ++i) {
        A.push_back(std::vector<int>(size+1));
        for(size_t x = 0; x <= size; ++x) {
            A[i][x] = calculateDecision(A, items, i, x);
        }
    }
    return A[items.size()-1][size];
}

int main() {
    size_t size;
    auto items = getItems(size, "class_example.txt");

    std::cout << "Knapsack for class exercise (expect 8) = " << knapsack(size, items) << std::endl;;

    auto items2 = getItems(size, "knapsack1.txt");
    std::cout << "Knapsack for HW1 = " << knapsack(size, items2) << std::endl;

    /*
    auto items3 = getItems(size, "knapsack_big.txt");
    std::cout << "Knapsack for HW2 = " << knapsack(size, items3) << std::endl;
    */
}
