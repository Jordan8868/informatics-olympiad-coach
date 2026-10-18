// stress-test.cpp —— 对拍骨架（Windows / Linux 通用，C++17）
//
// 用法：
//   1. 把 generator、暴力、正解分别编译成 gen.exe / brute.exe / fast.exe
//   2. 改下面的三个路径
//   3. g++ -O2 -std=c++17 stress-test.cpp -o stress && ./stress 1000
//
// 它做三件事：造数据 → 跑两份程序 → diff。不同就停下并保留现场。
// 关键不是"跑起来"，而是"造得出能杀死的样例"：小数据、极端数据、随机数据轮着来。
//
// 注意：Windows 下 system() 返回的是退出码，不是程序输出；所以这里全部走文件。

#include <bits/stdc++.h>
using namespace std;

const string GEN   = "gen.exe";
const string BRUTE = "brute.exe";
const string FAST  = "fast.exe";

string run(const string& cmd) {
    // 返回空串表示执行失败；调用方负责报错
    int code = system(cmd.c_str());
    return code == 0 ? "" : "exit " + to_string(code);
}

int main(int argc, char** argv) {
    int rounds = argc > 1 ? atoi(argv[1]) : 200;
    for (int t = 1; t <= rounds; ++t) {
        string err;
        if (!(err = run(GEN + " > in.txt")).empty()) {
            printf("[gen] %s\n", err.c_str());
            return 1;
        }
        if (!(err = run(BRUTE + " < in.txt > out1.txt")).empty()) {
            printf("[brute] round %d %s\n", t, err.c_str());
            return 1;
        }
        if (!(err = run(FAST + " < in.txt > out2.txt")).empty()) {
            printf("[fast] round %d %s\n", t, err.c_str());
            return 1;
        }
        if (system("fc out1.txt out2.txt > nul 2> nul") != 0 &&
            system("diff -q out1.txt out2.txt > /dev/null 2>&1") != 0) {
            printf("WA on round %d\n", t);
            printf("--- input (in.txt) ---\n");
            system("type in.txt 2> nul || cat in.txt");
            printf("--- brute (out1.txt) vs fast (out2.txt) ---\n");
            system("type out1.txt 2> nul || cat out1.txt");
            system("type out2.txt 2> nul || cat out2.txt");
            return 1;
        }
        if (t % 50 == 0) printf("round %d ok\n", t);
    }
    printf("all %d rounds passed\n", rounds);
    return 0;
}
