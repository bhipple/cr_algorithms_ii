#include <algorithm>
#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

typedef std::pair<int, float> Item;
typedef std::vector<Item> ItemVec;
typedef std::vector<std::vector<float>> DP;

ItemVec getItems(std::string fileName) {
    ItemVec items;

    std::ifstream myfile;  // Uses RAII automatically!
    myfile.open(fileName);
    if(myfile.is_open()) {
        std::string line;
        while(getline(myfile, line)) {
            std::string key, p;
            std::stringstream ss(line);
            ss >> key >> p;
            Item item = std::make_pair(std::stoi(key), std::stof(p));
            items.push_back(item);
        }
    }

    return items;
}

float optimalTreeCost(const ItemVec& items) {
    DP A;

    size_t n = items.size();
    for(size_t i = 0; i < items.size(); ++i) {
        A.push_back(std::vector<float>(items.size()));
    }

    for(size_t s = 0; s < n; ++s) { // Size of the subproblem
        for(size_t i = 0; i < n - s; ++i) { // Staring index
            float min = std::numeric_limits<float>::max();
            float constTerm = std::accumulate(items.begin() + i, items.begin() + i + s + 1, 0.0,
                [](const float& acc, const Item& next) { return acc + next.second; });

            // Try every root
            for(size_t r = i; r <= s + i; ++r) {
                float leftSubtree = 0;
                float rightSubtree = 0;
                if(r > 0 && i <= r-1) { leftSubtree = A[i][r-1]; }
                if(r+1 < n && i <= r+1) { rightSubtree = A[i][r+1]; }
                min = std::min(min, leftSubtree + rightSubtree);
            }


            A[i][i+s] = min + constTerm;
        }
    }
    return A[0][n-1];
}

int main() {
    auto items = getItems("optimal_tree.txt");

    for(auto item : items) {
        std::cout << "Item: " << item.first << "," << item.second << std::endl;
    }

    std::cout << "Cost: " << optimalTreeCost(items);
}
