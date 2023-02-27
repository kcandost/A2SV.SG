class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        m,m_year,count = 0,0,0
        peep = []

        for birth, death in logs: peep += (birth, 1), (death, -1)
        peep.sort()

        for year, effect in peep:
            count += effect
            if count > m: m,m_year = count,year
        return m_year
