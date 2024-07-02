from nada_dsl import *

def new_nada_program():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")  # Adding another party

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))  # Using different parties

    # Computation: Here you can perform operations on my_int1 and my_int2
    result = my_int1 + my_int2  # Example addition operation

    return [Output(result, "my_output", party1)]  # Returning the result as an output

# Example usage
if __name__ == "__main__":
    program = new_nada_program()
    print(program)
