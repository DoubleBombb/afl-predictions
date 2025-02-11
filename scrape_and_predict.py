"""
scrape_and_predict.py

This script:
1) Pretends to scrape (or loads) AFL data.
2) Runs a 'prediction' step (placeholder logic).
3) Generates 'predictions_output.html' to be published by GitHub Pages.
"""

import datetime

def fake_scrape():
    """
    In a real scenario, you'd use requests + BeautifulSoup or an API call
    to get AFL data. We'll just return a static list as an example.
    """
    afl_matches = [
        {"home": "Geelong", "away": "Carlton", "venue": "MCG"},
        {"home": "Sydney", "away": "Essendon", "venue": "SCG"},
        {"home": "Melbourne", "away": "Hawthorn", "venue": "MCG"},
    ]
    return afl_matches

def fake_predict(matches):
    """
    Placeholder prediction logic.
    Real logic: you might load a trained model, then pass in features.
    """
    predictions = []
    for match in matches:
        # We'll randomly say "Home team wins" for this demo
        pred_winner = match["home"]
        predictions.append({
            "home": match["home"],
            "away": match["away"],
            "venue": match["venue"],
            "predicted_winner": pred_winner
        })
    return predictions

def generate_html(predictions):
    """
    Creates a simple HTML page showing the predictions.
    """
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Basic HTML template
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>AFL Predictions</title>
</head>
<body>
    <h1>AFL Predictions - {today}</h1>
    <table border="1" cellpadding="5" style="border-collapse: collapse;">
        <tr>
            <th>Home</th>
            <th>Away</th>
            <th>Venue</th>
            <th>Predicted Winner</th>
        </tr>
    """

    for p in predictions:
        html_content += f"""
        <tr>
            <td>{p["home"]}</td>
            <td>{p["away"]}</td>
            <td>{p["venue"]}</td>
            <td>{p["predicted_winner"]}</td>
        </tr>
        """

    html_content += """
    </table>
    <p style="margin-top:20px;font-size:small;">
      <em>Note: These are placeholder predictions. Replace with your real logic!</em>
    </p>
</body>
</html>
"""
    # Write to file
    with open("predictions_output.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def main():
    matches = fake_scrape()
    predictions = fake_predict(matches)
    generate_html(predictions)

if __name__ == "__main__":
    main()
