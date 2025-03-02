# Time complexity O(V * N)

import dataclasses
from typing import Collection, Tuple, Deque
from collections import deque

@dataclasses.dataclass(frozen=True)
class Jewelry:
    value: int
    volumn: int
    quantity: int

def _compare_candidate(j: Jewelry, c1, c2) -> bool:
    # if c1 better than c2
    vol1, val1 = c1
    vol2, val2 = c2
    assert vol2 > vol1
    # return val1 + (vol2 - vol1) // j.volumn * j.value >= val2
    return val1 * j.volumn + (vol2 - vol1) * j.value >= val2 * j.volumn


@dataclasses.dataclass
class Group:
    dq: Deque[Tuple[int, int]] = dataclasses.field(default_factory=deque)  # [current_volumn, current_value]
    
    @classmethod
    def init(cls, j: Jewelry, dp, init_volumn: int):
        group = cls()
        for i in range(1, j.quantity+1):
            candidate_volumn = init_volumn - i * j.volumn
            if candidate_volumn < 0:
                break
            group.add_candidate(j, candidate_volumn, dp[candidate_volumn])
        return group
    
    def add_candidate(self, j: Jewelry, volumn: int, value: int):
        candidate = (volumn, value)
        while self.dq and _compare_candidate(j, candidate, self.dq[0]):
            self.dq.popleft()
        self.dq.appendleft(candidate)
    
    def pop_deprecate_candidate(self):
        self.dq.pop()

def solve(jewelris: Collection[Jewelry], total_volumn: int):
    # dp[volumn] = max_value
    dp = [0] * (total_volumn+1)
    for j in jewelris:
        # print(j)
        groups_by_no = [None for _ in range(j.volumn)]
        for v in range(total_volumn, -1, -1):
            group_no = v % j.volumn
            group = groups_by_no[group_no]
            if group is None:
                group = Group.init(j, dp, v)
                # print('Init', v, group)
                groups_by_no[group_no] = group
            else:
                # try extend candidate
                candidate_volumn = v - j.quantity * j.volumn
                if candidate_volumn >= 0:
                    group.add_candidate(j, candidate_volumn, dp[candidate_volumn])
            if not group.dq:
                break
            best_vol, best_val = group.dq[-1]
            # print('DEBUGGG', v, best_vol, best_val)
            if best_vol == v:
                group.pop_deprecate_candidate()
                continue
            dp[v] = max(dp[v], best_val + (v - best_vol) // j.volumn * j.value)
        
        # print(dp)
    
    return max(dp)
    
def read_ints():
    return map(int, input().split())

N, V = read_ints()
js = [Jewelry(*read_ints()) for _ in range(N)]

print(solve(js, V))
    
