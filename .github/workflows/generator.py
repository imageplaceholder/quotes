import concurrent.futures
from datetime import datetime
import json
import requests
from html2image import Html2Image

hti = Html2Image(
    size=(780, 740),
    custom_flags=[
        "--virtual-time-budget=1000",
        "--hide-scrollbars",
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--default-background-color=00000000",
    ],
)

tags = [
    "business",
    "change",
    "character",
    "competition",
    "conservative",
    "courage",
    "education",
    "faith",
    "family",
    "famous-quotes",
    "film",
    "freedom",
    "friendship",
    "future",
    "happiness",
    "history",
    "honor",
    "humorous",
    "inspirational",
    "leadership",
    "life",
    "literature",
    "love",
    "motivational",
    "nature",
    "pain",
    "philosophy",
    "politics",
    "power-quotes",
    "religion",
    "science",
    "self",
    "self-help",
    "social-justice",
    "spirituality",
    "sports",
    "success",
    "technology",
    "time",
    "truth",
    "virtue",
    "war",
    "wisdom",
]


def generate_single_image(tag):
  # Fetch data inside Python to ensure it's ready before rendering
  try:
    response = requests.get(
        f"https://johndturn-quotableapiproxy.web.val.run/random?tags={tag}",
        timeout=10,
    )
    data = response.json()
    quote = data[0]["content"]
    author = data[0]["author"]
  except Exception as e:
    print(f"Error fetching quote for {tag}: {e}")
    quote = "Could not load quote."
    author = "Unknown"

  html_content = f"""
    <link href="https://fonts.googleapis.com/css?family=Fugaz+One" rel="stylesheet">
    <div class="container text-center">
      <div class="quotes text-center">
        <span class="quote">{quote}</span>
        <br/><br/>
        <span class="author">-{author}</span>
      </div>
    </div>
    """

  css_content = """
    body {
        background: url(https://images.unsplash.com/photo-1493246507139-91e8fad9978e?dpr=1.25&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=); 
        background-size: cover;
        background-color: transparent;
        color: white;
        font-family: Garamond;
    }
    .quotes {
        background-color: black;
        width: 80%;
        margin: 60px auto;
        padding: 30px;
        border: 3px solid white;
        border-radius: 5px;
        box-shadow: 0 0 20px rgba(0,0,0,0.9);
        min-height: 400px;
        font-family: Courier;
    }
    .quote {
        font-size: 40px;
    }
    .author {
        font-size: 50px;
    }
    """

  hti.screenshot(
      html_str=html_content, css_str=css_content, save_as=f"{tag}.png"
  )


def generate():
  # Reduced max_workers to 4 to prevent crashing the headless browser environment
  with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(generate_single_image, tags)


if __name__ == "__main__":
  print("Starting image generation...")
  generate()

  # Create data.json map
  data = {}
  for item in tags:
    data[item] = f"https://imageplaceholder.github.io/quotes/{item}.png"

  last_updated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  data_to_dump = {"lastUpdated": last_updated_time, "quotes": data}

  with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data_to_dump, f, ensure_ascii=False, indent=4)

  print("Done! data.json updated.")
