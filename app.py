import gradio as gr

# Bubble Sort Algorithm
def bubble_sort(arr):
    steps = []  # To record every steps 
    a = arr.copy()
    n = len(a)
# Algorithm Start
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            steps.append(a.copy())  # save the status

    return a, steps
# This is a test
def test_bubble_sort():
    """Test function for bubble sort algorithm"""
    test_cases = [
        ([2, 34, 25, 12, 22, 11, 90], "Random array"),
        ([1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], "Reverse sorted"),
        ([12], "Single element"),
        ([], "Empty array"),
        ([2, 2, 2, 2], "All equal elements")
    ]
    
    print("Testing Bubble Sort Implementation")
    print("=" * 50)
    
    all_passed = True
    for arr, description in test_cases:
        sorted_arr, steps = bubble_sort(arr)
        expected = sorted(arr.copy())
        
        if sorted_arr == expected:
            print(f"  PASS: {description}")
            print(f"  Input: {arr}")
            print(f"  Output: {sorted_arr}")
            print(f"  Steps taken: {len(steps)}")
        else:
            print(f"✗ FAIL: {description}")
            print(f"  Expected: {expected}")
            print(f"  Got: {sorted_arr}")
            all_passed = False
        print()
    
    return all_passed

# Testing
if __name__ == "__main__":
    if test_bubble_sort():
        print("All tests passed!")
    else:
        print("Some tests failed!")


# Gradio UI Function 
def run_bubble_sort(text):
    try:
        arr = list(map(int, text.split(",")))
    except:
        return "Please enter corret numbers, for example: 5,3,1,4", []

    sorted_arr, steps = bubble_sort(arr)
    return str(sorted_arr), steps


# Gradio App Layout 
with gr.Blocks() as demo:
    gr.Markdown("# Bubble Sort Simulator\n Enter numbers，and I will demonstrate the entire process of bubble sort.")

    input_box = gr.Textbox(label="Enter numbers (separated by commas)", placeholder="for example：5,3,1,4,2")
    output_sorted = gr.Textbox(label="Final result")
    output_steps = gr.JSON(label="changes（for learning demonstrate）")

    run_btn = gr.Button("Run Bubble Sort")
    run_btn.click(run_bubble_sort, inputs=input_box, outputs=[output_sorted, output_steps])

demo.launch()
