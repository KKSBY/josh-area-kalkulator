import streamlit as st

st.title("📐 Area Calculator")
st.write("Choose a shape and enter the required dimensions.")

# Functions
def square(side):
    return side ** 2

def rectangle(width, length):
    return width * length

def triangle(base, height):
    return (base * height) / 2

def circle(radius):
    return 3.14 * (radius ** 2)

def kite(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def trapezium(side1, side2, height):
    return ((side1 + side2) * height) / 2


# Shape selection
shape = st.selectbox(
    "Choose a shape",
    (
        "Square",
        "Rectangle",
        "Triangle",
        "Circle",
        "Kite",
        "Trapezium",
    ),
)

# Input fields based on shape
if shape == "Square":
    side = st.number_input("Enter the side length", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of the square = {square(side)}")

elif shape == "Rectangle":
    width = st.number_input("Enter the width", min_value=0.0)
    length = st.number_input("Enter the length", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of the rectangle = {rectangle(width, length)}")

elif shape == "Triangle":
    base = st.number_input("Enter the base", min_value=0.0)
    height = st.number_input("Enter the height", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of the triangle = {triangle(base, height)}")

elif shape == "Circle":
    radius = st.number_input("Enter the radius", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of the circle = {circle(radius)}")

elif shape == "Kite":
    diagonal1 = st.number_input("Enter the first diagonal", min_value=0.0)
    diagonal2 = st.number_input("Enter the second diagonal", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of the kite = {kite(diagonal1, diagonal2)}")

elif shape == "Trapezium":
    side1 = st.number_input("Enter the first parallel side", min_value=0.0)
    side2 = st.number_input("Enter the second parallel side", min_value=0.0)
    height = st.number_input("Enter the height", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of the trapezium = {trapezium(side1, side2, height)}")
