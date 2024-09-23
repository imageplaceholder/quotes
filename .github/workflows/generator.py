import time
import concurrent.futures

from html2image import Html2Image
hti = Html2Image(size=(780, 740),  custom_flags=['--virtual-time-budget=200', '--hide-scrollbars'])

tags = ["business", "change", "character", "competition", "conservative", "courage", "education", "faith", "family", "famous-quotes", "film", "freedom", "friendship", "future", "happiness", "history", "honor", "humor", "humorous", "inspirational", "leadership", "life", "literature", "love", "motivational", "nature", "pain", "philosophy", "politics", "power-quotes", "religion", "science", "self", "self-help", "social-justice", "spirituality", "sports", "success", "technology", "time", "truth", "virtue", "war", "wisdom"]

def generate():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = [
            executor.submit(
                hti.screenshot,
                html_str=f"""<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" crossorigin="anonymous"></script>
<style>
</style>
<link href="https://fonts.googleapis.com/css?family=Fugaz+One" rel="stylesheet">
<div class="container text-center">
 
  <div class="quotes text-center">
		<span class="quote"></span>
    <br/>
    <span class="author"></span>
  </div>
  
</div>
<script>
  $(document).ready(function() {{
  var quote;
  var author;
  
  function getQuote(){{    
    var forismaticAPI = "https://johndturn-quotableapiproxy.web.val.run/random?tags={i}";  
    
    $.getJSON(forismaticAPI, function(data) {{
      quote = data.content;
      author = data.author;
       $(".quote").text(quote);
       $(".author").text("-"+author);
    }});   
  }}; //getQuote function
  
    $("#tweet").on("click", function(){{
      window.open("https://twitter.com/intent/tweet?text=" + quote + " -" + author);
    }});
    $("#newQuote").on("click", function(){{
    getQuote();
    }});
  
    getQuote();
}}); //docready
</script>""",
                # url='https://www.python.org',
                css_str="""   body{
 background: url(https://images.unsplash.com/photo-1493246507139-91e8fad9978e?dpr=1.25&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=); 
 background-size: cover;
	    background-color: transparent;
  color: white;
  font-family: Garamond;
}
.introduction{
	text-align: center;	
}
h1{
  font-family: 'Fugaz One', cursive;
  font-size: 50px;
  text-shadow: 5px 4px black, -1px -1px #444;
}
h2{
  font-family: 'Fugaz One', cursive;
  font-size: 20px;
}
a{
  color: red;
  text-decoration:underline;
}
a:hover{
  color:black;
  text-decoration:none;
}
p{
  padding: 30px;
  font-size: 20px;
}
button{
	margin: 0 auto;
  box-shadow: 0 0 10px rgba(0,0,0,0.6);
  font-family: Garamond;
}
button:hover{
  color: red;
  border: 1px solid red;
}
.quotes{
  background-color: black;
  width: 80%;
  margin: 60px auto;
  padding: 30px;
  border: 3px solid white;
  border-radius: 5px;
  box-shadow: 0 0 20px rgba(0,0,0,0.9);
  min-height:400px;
  font-family: Courier;
}
.quote{
    font-size:40px;
}
.author{
  font-size: 50px;
}""",
                save_as=f'{i}.png',
            )
            for i in tags
        ]
	
	

generate()

import json
from datetime import datetime

data = {}
for item in tags:
    data[item] = f'https://imageplaceholder.github.io/quotes/{item}.png'

# Add lastUpdated timestamp
last_updated_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data_to_dump = {'lastUpdated': last_updated_time, 'quotes': data}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data_to_dump, f, ensure_ascii=False, indent=4)

