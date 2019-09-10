vector<int> OutputOrdered(Container& ct) {
    vector<int> res;
    stack<int> stk;
    while (!ct.isEmpty()) {
        int cur = ct.get();
        if (!stk.empty() && cur > stk.top()) {
            res.push_back(stk.top()); stk.pop();
        }
        stk.push(cur);
    }
    while (!stk.empty()) {
        res.push_back(stk.top());
        stk.pop();
    }
    return res;
}