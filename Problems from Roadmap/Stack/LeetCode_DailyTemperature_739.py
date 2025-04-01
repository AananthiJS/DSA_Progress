class Solution:
    def dailyTemperatures(self, temperatures) :
        #BRUTE FORCE APPROACH
        answer = []

        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                if j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
                    count = 0
                    break         
                elif temperatures[j] > temperatures[i]:
                    count += 1
                    break
                elif temperatures[j] <= temperatures[i]:
                    count += 1 
            answer.append(count)

        return answer