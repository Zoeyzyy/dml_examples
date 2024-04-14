'''
generate_sum_by_time.py:
目的： 生成Sum_by_Time的数据0.01 0.001 0.0001粒度，以主节点对齐时间

方法：
1. 主函数：不同粒度, !! 修改node = 4

'''

from util import get_files_by_suffix, read_th_line, count_lines, time_to_float, remove_last_char_if_not_digit, create_file

def generate_sum_by_time(time_step, node):
    filenames = get_files_by_suffix("./packet", ".txt")
    
    master_step_line_number = count_lines("./master/step.txt")
    start_time = read_th_line("./master/step.txt", 0).split[1]
    end_time = read_th_line("./master/step.txt", master_step_line_number - 1).split[1]
    
    float_time_step = time_step.replace('_', '.')
    len_sum_by_time = (time_to_float(end_time) - time_to_float(start_time)) / time_to_float(float_time_step) + 1
    sum_by_time = [0] * len_sum_by_time
    
    for filename in filenames:
        # 打开文件
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "seq" in line:
                    line = line.split()
                    current_time = time_to_float(line[0])
                    time_index = (int)((current_time - time_to_float(start_time)) / time_to_float(float_time_step))
                    # 寻找"length" 的index
                    length_index = line.index("length")
                    if time_index >= 0 and time_index < len_sum_by_time:
                        sum_by_time[time_index] += remove_last_char_if_not_digit(line[length_index + 1])

            
            # 存储到文件中
            from_to = filename.split("_")[3]
            storename = "./Sum_by_Time/Sum_by_time_node" + str(node) + "_" + from_to + "_" + time_step
            create_file(storename)
            # sum_by_time记录到storefile中，每一行一个数据
            with open(storename, 'w') as f:
                for i in sum_by_time:
                    f.write(str(i) + '\n')   
                

# 主函数
if __name__ == '__main__':
    time_steps = ["0_01", "0_001", "0_0001"]
    node = 4
    for time_step in time_steps:
        generate_sum_by_time(time_step, node)