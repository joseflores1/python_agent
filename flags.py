import sys

def check_args(args: list):
    ## Dict with predefined args, first element of the key contains possible args to save, second one allows to check if the flag was input,
    # third one tells how many args it expects (let's not deal with possible "infinite args", we would establish a maximum, I think)
    defined_flags = {
        "--verbose": [None, False, 0],
    }

    #$ If there are no args we simply return the dict with all booleans set to False
    if len(args) == 0:
        return defined_flags
  
    ## Counter that will keep track of the current arg we are dealing with
    i = 0
    ## While there are args left to process
    while i < len(args):
        ## Saving the current position to save the args into the dict
        j = i

        ## Saving the flag name for error message
        flag_name = args[i]

        ## args[i] will always start with -- (possible flag), so we check if it is a valid flag
        if not args[i] in defined_flags:
            sys.exit(f"Error: invalid [{args[i]}] flag\nUsage: python main.py <prompt> [--args...]")
        else:
            defined_flags[args[i]][1] = True

        ## Defining variables to keep track of input args for the current flag, ensuring a valid number of these
        expected = defined_flags[args[i]][2] 
        actual = 0
        ## List for saving args into dict
        input_args = []

        ## If the flag expects args
        if expected > 0:
            # We deal with the args that come after the flag
            rest_of_args = args[i + 1:]
            # We increment the counter to be in the element just right of the flag
            i += 1
            # We process the rest of args (which may contain future flags) until we get an error for invalid number of flags or we receive
            # a correct number of these.
            for flag in rest_of_args:
                if not flag.startswith("--"): 
                    input_args.append(flag)
                    actual += 1
                    if actual > expected:
                        sys.exit(f"Error: invalid number of arguments for {flag_name} flag, expected {expected}.")
                    i += 1
                elif actual == expected:
                    break
            ## We got less args than expected
            if actual < expected:
                sys.exit(f"Error: invalid number of arguments for {flag_name} flag, expected {expected}.")
        ## If the flag doesn't expect args we move on to the next arg.
        else:
            i += 1

        ## We save the args into the flags dict
        defined_flags[args[j]][0] = input_args

    ## We return the dict
    return defined_flags