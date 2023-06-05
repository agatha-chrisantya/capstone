import pandas as pd
import streamlit as st
import numpy as np
# import altair as alt
import plotly_express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = "U.S. Food Import",
    layout = "wide"
)

opt = option_menu(
    menu_title = None,
    options = ["Summary", "Data"],
    orientation = "horizontal"
)

if opt == "Summary":
    st.title("U.S. Food Import")

    df = pd.read_excel("FoodImports_Edited.xlsx", "FoodValue")

    curr_year = df["Year"].max()
    prev_year = curr_year - 1
    
    total_foods = pd.pivot_table(
        data = df,
        index = "Year",
        values = "U.S. imports"
    ).reset_index()

    col_name = list(df.columns.values)
    source = []
    for i in range(2, 16):
        source.append(col_name[i])

    food = pd.pivot_table(
        data = df,
        index = "Year",
        values = source
    ).reset_index()

    ##total_now = st.columns(1)

    curr_imp = total_foods.loc[total_foods["Year"] == curr_year, "U.S. imports"].values[0]
    prev_imp = total_foods.loc[total_foods["Year"] == prev_year, "U.S. imports"].values[0]
    
    imp_diff = 100 * (curr_imp - prev_imp) / prev_imp

    st.metric(
        label = "Total Imports",
        value = curr_imp,
        delta = f"{imp_diff:.2f}"
    )

    st.header("Total Imports")
    fig = px.line(total_foods, x = "Year", y = "U.S. imports")
    st.plotly_chart(fig, use_container_width = True)

    st.header("Source")
    fig2 = px.line(food, x = "Year", y = source)
    st.plotly_chart(fig2, use_container_width =True)

else:
    with st.sidebar:
        chart = st.selectbox("Sources", ("Animals", "Meats", "Fish", "Vegetables",
                            "Dairy","Fruits","Nuts", "Coffee", "Grains",
                            "Vegetable Oil", "Sweets", "Cocoa", "Beverages", "Other"))
    if chart == "Animals":
        coms = st.selectbox("Comodities", ("Bovine", "Swine", "Sheep and Goat", "Live Poultry", "Bird Eggs"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Animals")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Bovine":
            for i in range(6, 8):
                kind.append(col_name2[i])
            bovine = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(bovine, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Swine":
            for i in range(10, 11):
                kind.append(col_name2[i])
            swine = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(swine, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Sheep and Goat":
            for i in range(13, 14):
                kind.append(col_name2[i])
            s_g = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(s_g, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Live Poultry":
            for i in range(16, 17):
                kind.append(col_name2[i])
            poultry = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(poultry, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(19, len(col_name2)-2):
                kind.append(col_name2[i])
            eggs = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(eggs, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Meats":
        coms = st.selectbox("Comodities", ("Fresh or Chilled Red Meats",
                                           "Frozen Red Meats", "Fowl and Other Meats",
                                           "Prepared Meats"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Meats")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Fresh or Chilled Red Meats":
            for i in range(11, 17):
                kind.append(col_name2[i])
            red = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(red, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Frozen Red Meats":
            for i in range(20, 26):
                kind.append(col_name2[i])
            frozen = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(frozen, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Fowl and Other Meats":
            for i in range(29, 33):
                kind.append(col_name2[i])
            fowl = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(fowl, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(36, len(col_name2)-3):
                kind.append(col_name2[i])
            prep = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(prep, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Fish":
        coms = st.selectbox("Comodities", ("Whole Fish (Fresh, Chilled or Frozen)",
                                           "Fish Fillet and Mince", "Shellfish (Fresh or Frozen)",
                                           "Prepared Fish and Shellfish"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Fish")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Whole Fish (Fresh, Chilled or Frozen)":
            for i in range(11, 17):
                kind.append(col_name2[i])
            fresh = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(fresh, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Fish Fillet and Mince":
            for i in range(20, 26):
                kind.append(col_name2[i])
            fillet = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(fillet, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Shellfish (Fresh or Frozen)":
            for i in range(29, 37):
                kind.append(col_name2[i])
            shellfish = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(shellfish, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(40, len(col_name2)-3):
                kind.append(col_name2[i])
            prep = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(prep, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Vegetables":
        coms = st.selectbox("Comodities", ("Fresh Vegetables", "Frozen Vegetables",
                                           "Dried Vegetables", "Prepared Vegetables"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Vegetables")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Fresh Vegetables":
            for i in range(11, 17):
                kind.append(col_name2[i])
            fresh = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(fresh, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Frozen Vegetables":
            for i in range(20, 26):
                kind.append(col_name2[i])
            frozen = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(frozen, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Dried Vegetables":
            for i in range(29, 34):
                kind.append(col_name2[i])
            dried = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(dried, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(37, len(col_name2)-3):
                kind.append(col_name2[i])
            prep = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(prep, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Dairy":
        coms = st.selectbox("Comodities", ("Cheese", "Yogurt, Buttermilk, or Whey",
                                           "Milk and Cream", "Butter or Spreads"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Dairy")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Cheese":
            for i in range(12, 19):
                kind.append(col_name2[i])
            cheese = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(cheese, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Yogurt, Buttermilk, or Whey":
            for i in range(22, 29):
                kind.append(col_name2[i])
            yogurt = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(yogurt, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Milk and Cream":
            for i in range(32, 38):
                kind.append(col_name2[i])
            milk = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(milk, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(41, len(col_name2)-3):
                kind.append(col_name2[i])
            butter = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(butter, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Fruits":
        coms = st.selectbox("Comodities", ("Fresh or Chilled Fruits", "Bananas and Plantains",
                                           "Frozen Fruits", "Dried, Prepared, or Preserved Fruits",
                                           "Fruit Juices"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Fruits")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Fresh or Chilled Fruits":
            for i in range(14, 24):
                kind.append(col_name2[i])
            fresh = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(fresh, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Bananas and Plantains":
            for i in range(27, 33):
                kind.append(col_name2[i])
            banana = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(banana, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Frozen Fruits":
            for i in range(36, 42):
                kind.append(col_name2[i])
            frozen = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(frozen, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Dried, Prepared, or Preserved Fruits":
            for i in range(45, 51):
                kind.append(col_name2[i])
            dried = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(dried, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(54, len(col_name2)-3):
                kind.append(col_name2[i])
            juice = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(juice, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Nuts":
        coms = st.selectbox("Comodities", ("Tree Nuts", "Cashew Nuts",
                                           "Prepared Tree Nuts", "Ground Nuts"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Nuts")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Tree Nuts":
            for i in range(13, 22):
                kind.append(col_name2[i])
            tree = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(tree, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Cashew Nuts":
            for i in range(25, 32):
                kind.append(col_name2[i])
            cashew = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(cashew, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Prepared Tree Nuts":
            for i in range(35, 42):
                kind.append(col_name2[i])
            prep = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(prep, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(45, len(col_name2)-3):
                kind.append(col_name2[i])
            ground = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(ground, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Coffee":
        coms = st.selectbox("Comodities", ("Coffee Beans (Unroasted)", "Coffee (Roasted and Instant)",
                                           "Coffee Extracts and Preparations", "Tea and Mate", "Spices"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Coffee")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Coffee Beans (Unroasted)":
            for i in range(11, 17):
                kind.append(col_name2[i])
            beans = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(beans, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Coffee (Roasted and Instant)":
            for i in range(20, 25):
                kind.append(col_name2[i])
            coffee = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(coffee, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Coffee Extracts and Preparations":
            for i in range(28, 32):
                kind.append(col_name2[i])
            extract = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(extract, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Tea and Mate":
            for i in range(35, 39):
                kind.append(col_name2[i])
            tea = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(tea, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(42, len(col_name2)-3):
                kind.append(col_name2[i])
            spice = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(spice, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Grains":
        coms = st.selectbox("Comodities", ("Bulk Grains", "Wheat and Products",
                                           "Rice and Products", "Milled Grain Products",
                                           "Cereal and Bakery Foods"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Grains")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Bulk Grains":
            for i in range(13, 20):
                kind.append(col_name2[i])
            bulk = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(bulk, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Wheat and Products":
            for i in range(23, 27):
                kind.append(col_name2[i])
            wheat = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(wheat, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Rice and Products":
            for i in range(30, 34):
                kind.append(col_name2[i])
            rice = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(rice, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Milled Grain Products":
            for i in range(37, 44):
                kind.append(col_name2[i])
            milled = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(milled, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(47, len(col_name2)-3):
                kind.append(col_name2[i])
            cereal = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(cereal, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Vegetable Oil":
        coms = st.selectbox("Comodities", ("Crude Vegetable Oils", "Refined Vegetable Oils",
                                           "Olive Oil", "Tropical Oils", "Oilseeds"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "VegOils")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Crude Vegetable Oils":
            for i in range(11, 17):
                kind.append(col_name2[i])
            crude = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(crude, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Refined Vegetable Oils":
            for i in range(20, 26):
                kind.append(col_name2[i])
            refined = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(refined, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Olive Oil":
            for i in range(29, 34):
                kind.append(col_name2[i])
            olive_oil = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(olive_oil, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Tropical Oils":
            for i in range(37, 43):
                kind.append(col_name2[i])
            tropical = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(tropical, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(46, len(col_name2)-3):
                kind.append(col_name2[i])
            oilseed = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(oilseed, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Sweets":
        coms = st.selectbox("Comodities", ("Sugar, Cane, and Beet", "Other Sweeteners and Syrups",
                                           "Confections"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Sweets")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Sugar, Cane, and Beet":
            for i in range(12, 19):
                kind.append(col_name2[i])
            sugar = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(sugar, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Other Sweeteners and Syrups":
            for i in range(22, 28):
                kind.append(col_name2[i])
            syrup = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(syrup, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(31, len(col_name2)-3):
                kind.append(col_name2[i])
            confection = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(confection, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Cocoa":
        coms = st.selectbox("Comodities", ("Cocoa Beans", "Choco Paste, Butter, and Powder",
                                           "Chocolate"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Cocoa")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Cocoa Beans":
            for i in range(11, 17):
                kind.append(col_name2[i])
            beans = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(beans, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Choco Paste, Butter, and Powder":
            for i in range(20, 28):
                kind.append(col_name2[i])
            paste = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(paste, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(31, len(col_name2)-3):
                kind.append(col_name2[i])
            choco = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(choco, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Beverages":
        coms = st.selectbox("Comodities", ("Wine", "Malt Beer",
                                           "Nonalcoholic Beverages",
                                           "Liquors and Liqueurs"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Beverages")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Wine":
            for i in range(13, 20):
                kind.append(col_name2[i])
            wine = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(wine, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Malt Beer":
            for i in range(23, 30):
                kind.append(col_name2[i])
            malt = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(malt, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Nonalcoholic Beverages":
            for i in range(33, 39):
                kind.append(col_name2[i])
            non_alc = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(non_alc, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(42, len(col_name2)-3):
                kind.append(col_name2[i])
            liq = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(liq, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
    elif chart == "Other":
        coms = st.selectbox("Comodities", ("Sauce, Soups, and Prepared Foods",
                                           "Essential Oils", "Animal and Other Fats",
                                           "Other Edible Products"))
        df2 = pd.read_excel("FoodImports_Edited.xlsx", "Others")
        col_name2 = list(df2.columns.values)
        kind = []
        if coms == "Sauce, Soups, and Prepared Foods":
            for i in range(1, 9):
                kind.append(col_name2[i])
            sauce = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(sauce, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Essential Oils":
            for i in range(12, 20):
                kind.append(col_name2[i])
            essen_oil = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(essen_oil, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        elif coms == "Animal and Other Fats":
            for i in range(23, 31):
                kind.append(col_name2[i])
            fat = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(fat, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
        else:
            for i in range(34, len(col_name2)-3):
                kind.append(col_name2[i])
            other = pd.pivot_table(
                data = df2,
                index = "Year",
                values = kind
            ).reset_index()
            fig3 = px.line(other, x = "Year", y = kind)
            st.plotly_chart(fig3, use_container_width =True)
