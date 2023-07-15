import streamlit as st
import random

def create_quiz():
    st.header("Quiz Creator")
    
    num_questions = st.number_input("Number of Questions", min_value=1, step=1)
    
    questions = []
    for i in range(num_questions):
        st.subheader(f"Question {i+1}")
        question = st.text_input(f"Enter Question {i+1}")
        options = st.text_input(f"Enter Options (comma-separated) for the question")
        options = [option.strip() for option in options.split(",")]
        answer = st.text_input(f"Enter Answer for Question {i+1}")
        
        questions.append({"question": question, "options": options, "answer": answer})
    
    if st.button("Generate Quiz"):
        return questions
    
    return None

def take_quiz(questions):
    st.header("Quiz")
    
    num_questions = len(questions)
    user_answers = []
    
    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}: {question['question']}")
        
        options = question['options']
        selected_option = st.selectbox("Select an option", options)
        user_answers.append(selected_option)
        
    if st.button("Submit Answers"):
        show_results(questions, user_answers)

def show_results(questions, user_answers):
    st.header("Quiz Results")
    
    num_questions = len(questions)
    num_correct = 0
    
    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}: {question['question']}")
        
        correct_answer = question['answer']
        user_answer = user_answers[i]
        
        if user_answer == correct_answer:
            st.write("Your answer: ", user_answer)
            st.write("Correct answer: ", correct_answer)
            st.write("Result: Correct!")
            num_correct += 1
        else:
            st.write("Your answer: ", user_answer)
            st.write("Correct answer: ", correct_answer)
            st.write("Result: Incorrect!")
        
        st.write("---")
    
    st.write(f"You scored {num_correct}/{num_questions} correct answers.")
    st.write("Thank you for taking the quiz!")

def main():
    st.title("Quiz Generator")
    st.sidebar.header("Menu")
    
    menu_options = ["Create Quiz", "Take Quiz"]
    selected_option = st.sidebar.selectbox("Select an option", menu_options)
    
    if selected_option == "Create Quiz":
        questions = create_quiz()
        if questions is not None:
            st.sidebar.success("Quiz generated successfully!")
    elif selected_option == "Take Quiz":
        if "questions" not in st.session_state:
            st.sidebar.warning("Please generate a quiz first.")
        else:
            take_quiz(st.session_state.questions)
    
    st.sidebar.write("---")
    st.sidebar.write("Powered by Streamlit")
    
if __name__ == "__main__":
    main()
