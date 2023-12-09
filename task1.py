def handler(input: dict, context: object) -> dict[str, any]:
    response = {}
    if not ('cpus' in context.env):
        context.env['cpus'] = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
    
    for i in range(0,16):
        if len(context.env['cpus'][i]) == 12:
            #print("cpu {}: Already have 12 percentages".format(str(i)))
            context.env['cpus'][i].pop(0)
            context.env['cpus'][i].append(input['cpu_percent-' + str(i)])
            #print("cpu {}: Removed first percentage and appended current percentage to list".format(str(i)))
        else:
            #print("cpu {}: Still does not have 12 percentages".format(str(i)))
            context.env['cpus'][i].append(input['cpu_percent-' + str(i)])
            #print("cpu {}: Added new percentage to list. Moving Average will be calculated with the currently stored percentages".format(str(i)))
        
        response["cpu-" + str(i)] = sum(context.env['cpus'][i]) / len(context.env['cpus'][i])
        #print("cpu {}: Moving Average calculated, result is: {}".format(str(i), str(response["cpu-" + str(i)])))

    response['traffic'] = input['net_io_counters_eth0-bytes_sent'] / (input['net_io_counters_eth0-bytes_sent'] + input['net_io_counters_eth0-bytes_recv'])
    response['memory'] = (input['virtual_memory-cached'] + input['virtual_memory-buffers']) / input['virtual_memory-total']
    #print(response)
    return response