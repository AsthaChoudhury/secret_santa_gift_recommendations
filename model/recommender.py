import pandas as pd


class GiftRecommender:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def get_recommendations(self, age, gender):
        gender_data = self.data[self.data['Gender'].str.lower()
                                == gender.lower()]
        age_data = gender_data[(gender_data['Age'] >= age - 5)
                               & (gender_data['Age'] <= age + 5)]

        if age_data.empty:
            print("No data available")
            return []

        product_counts = (age_data.groupby(
            'ProductName')['Quantity'].sum().sort_values(ascending=False).head(10))

        print("Top Products:", product_counts)
        recommendations = product_counts.index.tolist()
        if len(recommendations) < 10:
            general_popular_products = (
                self.data.groupby('ProductName')['Quantity']
                .sum()
                .sort_values(ascending=False)
                .head(10 - len(recommendations))
                .index.tolist()
            )
            recommendations.extend(general_popular_products)

        recommendations = list(dict.fromkeys(recommendations))[:10]
        return recommendations


if __name__ == "__main__":
    data_path = "data/Christmas Sales and Trends.csv"
    recommender = GiftRecommender(data_path)
    age = int(input("Enter the age: "))
    gender = input("Enter the gender(Male/Female/Other): ")
    recommendations = recommender.get_recommendations(age, gender)
    if recommendations:
        print("Recommended Products:", recommendations)
    else:
        print("No recommendations available.")
