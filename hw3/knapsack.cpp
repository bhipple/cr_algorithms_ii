#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

typedef std::pair<size_t, size_t> Item;
typedef std::vector<Item> ItemVec;
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
            Item item = std::make_pair(std::stoi(value), std::stoi(weight));
            items.push_back(item);
        }
    }

    return items;
}

int getRemainder(const Item& item, size_t x) {
    int remainder = static_cast<int>(x) - item.second;
    return remainder;
}

int calculateDecision(const std::vector<int>& last, const ItemVec& items, size_t i, size_t x) {
    int skipThis = 0;
    int useThis = 0;

    skipThis = last[x];

    int remainder = getRemainder(items[i], x);
    if(remainder >= 0) {
        useThis = items[i].first + last[remainder];
    }

    return std::max(skipThis, useThis);
}

int knapsack(size_t size, const ItemVec& items) {
    DP A;

    A.push_back(std::vector<int>(size+1));
    // Do the first column
    for(size_t x = 0; x < size+1; ++x) {
        int rem = getRemainder(items[0], x);
        if(rem > 0) {
            A[0][x] = rem;
        }
    }
    A.push_back(std::vector<int>(size+1));

    for(size_t i = 1; i < items.size(); ++i) {
        for(size_t x = 0; x <= size; ++x) {
            A[1][x] = calculateDecision(A[0], items, i, x);
        }
        std::swap(A[0], A[1]);
    }
    return A[0][size];
}

int main() {
    size_t size;
    auto items = getItems(size, "class_example.txt");

    std::cout << "Knapsack for class exercise (expect 8) = " << knapsack(size, items) << std::endl;;

    auto items2 = getItems(size, "knapsack1.txt");
    std::cout << "Knapsack for HW1 = " << knapsack(size, items2) << std::endl;

    auto items3 = getItems(size, "knapsack_big.txt");
    std::cout << "Knapsack for HW2 = " << knapsack(size, items3) << std::endl;
}
