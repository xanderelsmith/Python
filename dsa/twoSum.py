class TwoSum:
    def calculate_two_sum(self,nums:list[int],total):
        map={}
        
        for index in range(len(nums)):
            remainder=total - nums[index]      
            if(map.keys().__contains__(remainder)):
                
                return [index,remainder]
            map[nums[index]]=index
        
        
        
        
two_sum_object=TwoSum()
entities=two_sum_object.calculate_two_sum(nums=[1,2,4],total=6)
print(entities)

        