# Compass Digital AI Engineer Take-Home Exercise

## Overview
This project aims to automate and optimize the matching process between two product lists for a stakeholder operating convenience-store-like markets. Currently, the manual process of aligning internal product data with new, incoming products from suppliers is slow and inefficient. To address this, we will develop an intelligent, automated system that accurately matches products from both lists.

## Objective
The primary objective is to create a solution that matches external products (from suppliers) with internal items (from the stakeholder's existing inventory) based on identical manufacturer, name, and size attributes. The solution must leverage prompt engineering as part of the tech stack to enhance the matching accuracy.

### Key Deliverables
1. **Final Result**:  
   - A table that displays all external items along with their corresponding mapped internal product. If no match is found, the table should indicate `NULL` for the internal product.
   
2. **Presentation**:  
   - A short, non-technical presentation demonstrating how the system works.
   - Prepared materials (e.g., Jupyter notebooks) to discuss technical details when required.

3. **Bonus (Optional)**:  
   - Develop a simple front-end application using tools such as Streamlit or Gradio to enhance user interaction.

## Evaluation Criteria
The solution will be evaluated based on:
- The approach to exploring and understanding the datasets.
- The thought process behind the chosen solution.
- The effectiveness and accuracy of the matching system.
- The clarity and accessibility of the presentation for a non-technical audience.
- Additional points will be awarded for implementing a user-friendly front-end application.

## Approach
1. **Data Exploration**:  
   - Initial analysis of both datasets to identify patterns, key attributes, and potential challenges in matching.
   
2. **Prompt Engineering**:  
   - Develop a series of prompt engineering techniques to refine the matching process, ensuring exact matches based on manufacturer, name, and size.

3. **Automated Matching System**:  
   - Implement an intelligent system using machine learning or rule-based algorithms to match external products with internal items.
   - Generate a table with results, indicating matches and non-matches (`NULL`).

4. **Front-End Development (Optional)**:  
   - Build a simple, user-friendly front-end application using a tool like Streamlit or Gradio to allow stakeholders to interact with the matching results.

5. **Presentation Preparation**:  
   - Create a presentation that explains the process and outcome in a format suitable for non-technical stakeholders.

## Examples of Product Matches
To clarify the requirements, here are a few examples of correct and incorrect matches:

| External Product Name                    | Internal Product Name                                       | Status       |
|-------------------------------------------|-------------------------------------------------------------|--------------|
| DIET LIPTON GREEN TEA W/ CITRUS 20 OZ     | Lipton Diet Green Tea with Citrus (20oz)                    | Correct Match |
| CH-CHERRY CHS CLAW DANISH 4.25 OZ         | Cloverhill Cherry Cheese Bearclaw Danish (4.25oz)            | Correct Match |
| Hersheys Almond Milk Choco 1.6 oz         | Hersheys Milk Chocolate with Almonds (1.85oz)               | Wrong Match  |
| COOKIE PEANUT BUTTER 2OZ                  | Famous Amos Peanut Butter Cookie (2oz)                      | Wrong Match  |

## Conclusion
This project is a great opportunity to showcase problem-solving skills in the field of data engineering and AI. The focus will be on designing a robust and efficient solution that accurately maps products while demonstrating creativity and technical acumen in the approach taken.