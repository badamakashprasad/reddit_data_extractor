import requests
from bs4 import BeautifulSoup
from store_data import store_data
import datetime
txt = """
<h1 id="wiki_general_content"><strong>General Content</strong></h1>
<h2 id="wiki_gifs"><strong>Gifs</strong></h2>
<p><a href="/r/gifs" rel="nofollow">/r/gifs</a><br>
<a href="/r/behindthegifs" rel="nofollow">/r/behindthegifs</a><br>
<a href="/r/gif" rel="nofollow">/r/gif</a><br>
<a href="/r/Cinemagraphs" rel="nofollow">/r/Cinemagraphs</a><br>
<a href="/r/WastedGifs" rel="nofollow">/r/WastedGifs</a><br>
<a href="/r/educationalgifs" rel="nofollow">/r/educationalgifs</a><br>
<a href="/r/perfectloops" rel="nofollow">/r/perfectloops</a><br>
<a href="/r/highqualitygifs" rel="nofollow">/r/highqualitygifs</a><br>
<a href="/r/gifsound" rel="nofollow">/r/gifsound</a><br>
<a href="/r/combinedgifs" rel="nofollow">/r/combinedgifs</a><br>
<a href="/r/retiredgif" rel="nofollow">/r/retiredgif</a><br>
<a href="/r/michaelbaygifs" rel="nofollow">/r/michaelbaygifs</a><br>
<a href="/r/gifrecipes" rel="nofollow">/r/gifrecipes</a><br>
<a href="/r/mechanical_gifs" rel="nofollow">/r/mechanical_gifs</a><br>
<a href="/r/bettereveryloop" rel="nofollow">/r/bettereveryloop</a><br>
<a href="/r/gifextra" rel="nofollow">/r/gifextra</a><br>
<a href="/r/slygifs" rel="nofollow">/r/slygifs</a><br>
<a href="/r/gifsthatkeepongiving" rel="nofollow">/r/gifsthatkeepongiving</a><br>
<a href="/r/wholesomegifs" rel="nofollow">/r/wholesomegifs</a><br>
<a href="/r/noisygifs" rel="nofollow">/r/noisygifs</a><br>
<a href="/r/brokengifs" rel="nofollow">/r/brokengifs</a><br>
<a href="/r/loadingicon" rel="nofollow">/r/loadingicon</a><br>
<a href="/r/splitdepthgifs" rel="nofollow">/r/splitdepthgifs</a> </p>
<h3 id="wiki_people"><em>People</em></h3>
<p><a href="/r/blackpeoplegifs" rel="nofollow">/r/blackpeoplegifs</a><br>
<a href="/r/whitepeoplegifs" rel="nofollow">/r/whitepeoplegifs</a><br>
<a href="/r/asianpeoplegifs" rel="nofollow">/r/asianpeoplegifs</a><br>
<a href="/r/scriptedasiangifs" rel="nofollow">/r/scriptedasiangifs</a> </p>
<h3 id="wiki_reaction"><em>Reaction</em></h3>
<p><a href="/r/reactiongifs" rel="nofollow">/r/reactiongifs</a><br>
<a href="/r/shittyreactiongifs" rel="nofollow">/r/shittyreactiongifs</a> </p>
<h3 id="wiki_science"><em>Science</em></h3>
<p><a href="/r/chemicalreactiongifs" rel="nofollow">/r/chemicalreactiongifs</a><br>
<a href="/r/physicsgifs" rel="nofollow">/r/physicsgifs</a> </p>
<h4 id="wiki_nature"><em>Nature</em></h4>
<p><a href="/r/babyelephantgifs" rel="nofollow">/r/babyelephantgifs</a><br>
<a href="/r/weathergifs" rel="nofollow">/r/weathergifs</a> </p>
<h2 id="wiki_images"><strong>Images</strong></h2>
<p><a href="/r/pics" rel="nofollow">/r/pics</a><br>
<a href="/r/PhotoshopBattles" rel="nofollow">/r/PhotoshopBattles</a><br>
<a href="/r/perfecttiming" rel="nofollow">/r/perfecttiming</a><br>
<a href="/r/itookapicture" rel="nofollow">/r/itookapicture</a><br>
<a href="/r/Pareidolia" rel="nofollow">/r/Pareidolia</a><br>
<a href="/r/ExpectationVSReality" rel="nofollow">/r/ExpectationVSReality</a><br>
<a href="/r/dogpictures" rel="nofollow">/r/dogpictures</a><br>
<a href="/r/misleadingthumbnails" rel="nofollow">/r/misleadingthumbnails</a><br>
<a href="/r/FifthWorldPics" rel="nofollow">/r/FifthWorldPics</a><br>
<a href="/r/TheWayWeWere" rel="nofollow">/r/TheWayWeWere</a><br>
<a href="/r/pic" rel="nofollow">/r/pic</a><br>
<a href="/r/nocontextpics" rel="nofollow">/r/nocontextpics</a><br>
<a href="/r/miniworlds" rel="nofollow">/r/miniworlds</a><br>
<a href="/r/foundpaper" rel="nofollow">/r/foundpaper</a><br>
<a href="/r/images" rel="nofollow">/r/images</a> </p>
<h3 id="wiki_interesting"><em>Interesting</em></h3>
<p><a href="/r/mildlyinteresting" rel="nofollow">/r/mildlyinteresting</a> (see also: the <a href="http://www.reddit.com/r/ListOfSubreddits/wiki/mild" rel="nofollow">"Mild Network"</a>). Not all are active!<br>
<a href="/r/interestingasfuck" rel="nofollow">/r/interestingasfuck</a><br>
<a href="/r/damnthatsinteresting" rel="nofollow">/r/damnthatsinteresting</a><br>
<a href="/r/beamazed" rel="nofollow">/r/beamazed</a><br>
<a href="/r/reallifeshinies" rel="nofollow">/r/reallifeshinies</a> </p>
<h3 id="wiki_images.2Fgifs_of_women_.28sfw.29"><em>Images/Gifs of Women (SFW)</em></h3>
<p><a href="/r/gentlemanboners" rel="nofollow">/r/gentlemanboners</a><br>
<a href="/r/prettygirls" rel="nofollow">/r/prettygirls</a><br>
<a href="/r/hardbodies" rel="nofollow">/r/hardbodies</a><br>
<a href="/r/girlsmirin" rel="nofollow">/r/girlsmirin</a><br>
<a href="/r/thinspo" rel="nofollow">/r/thinspo</a><br>
<a href="/r/goddesses" rel="nofollow">/r/goddesses</a><br>
<a href="/r/shorthairedhotties" rel="nofollow">/r/shorthairedhotties</a><br>
<a href="/r/fitandnatural" rel="nofollow">/r/fitandnatural</a><br>
<a href="/r/wrestlewiththeplot" rel="nofollow">/r/wrestlewiththeplot</a><br>
<a href="/r/skinnywithabs" rel="nofollow">/r/skinnywithabs</a><br>
<a href="/r/bois" rel="nofollow">/r/bois</a><br>
<a href="/r/GentlemanBonersGifs" rel="nofollow">/r/GentlemanBonersGifs</a> </p>
<h4 id="wiki_asian"><em>Asian</em></h4>
<p><a href="/r/asiancuties" rel="nofollow">/r/asiancuties</a><br>
<a href="/r/asiangirlsbeingcute" rel="nofollow">/r/asiangirlsbeingcute</a> </p>
<h3 id="wiki_photoshop"><em>Photoshop</em></h3>
<p><a href="/r/PhotoshopBattles" rel="nofollow">/r/PhotoshopBattles</a><br>
<a href="/r/ColorizedHistory" rel="nofollow">/r/ColorizedHistory</a><br>
<a href="/r/reallifedoodles" rel="nofollow">/r/reallifedoodles</a><br>
<a href="/r/HybridAnimals" rel="nofollow">/r/HybridAnimals</a><br>
<a href="/r/colorization" rel="nofollow">/r/colorization</a> </p>
<h3 id="wiki_redditors.2Fselfies"><em>Redditors/Selfies</em></h3>
<p><a href="/r/amiugly" rel="nofollow">/r/amiugly</a><br>
<a href="/r/roastme" rel="nofollow">/r/roastme</a><br>
<a href="/r/rateme" rel="nofollow">/r/rateme</a><br>
<a href="/r/uglyduckling" rel="nofollow">/r/uglyduckling</a><br>
<a href="/r/prettygirlsuglyfaces" rel="nofollow">/r/prettygirlsuglyfaces</a> </p>
<h3 id="wiki_wallpapers"><em>Wallpapers</em></h3>
<p><a href="/r/wallpapers" rel="nofollow">/r/wallpapers</a><br>
<a href="/r/wallpaper" rel="nofollow">/r/wallpaper</a><br>
<a href="/r/Offensive_Wallpapers" rel="nofollow">/r/Offensive_Wallpapers</a> </p>
<h2 id="wiki_videos"><strong>Videos</strong></h2>
<p><a href="/r/videos" rel="nofollow">/r/videos</a><br>
<a href="/r/youtubehaiku" rel="nofollow">/r/youtubehaiku</a><br>
<a href="/r/artisanvideos" rel="nofollow">/r/artisanvideos</a><br>
<a href="/r/DeepIntoYouTube" rel="nofollow">/r/DeepIntoYouTube</a><br>
<a href="/r/nottimanderic" rel="nofollow">/r/nottimanderic</a><br>
<a href="/r/praisethecameraman" rel="nofollow">/r/praisethecameraman</a><br>
<a href="/r/killthecameraman" rel="nofollow">/r/killthecameraman</a> </p>
<hr>
<h1 id="wiki_discussion"><strong>Discussion</strong></h1>
<h2 id="wiki_general"><strong>General</strong></h2>
<p><a href="/r/ShowerThoughts" rel="nofollow">/r/ShowerThoughts</a><br>
<a href="/r/DoesAnybodyElse" rel="nofollow">/r/DoesAnybodyElse</a><br>
<a href="/r/changemyview" rel="nofollow">/r/changemyview</a><br>
<a href="/r/crazyideas" rel="nofollow">/r/crazyideas</a><br>
<a href="/r/howtonotgiveafuck" rel="nofollow">/r/howtonotgiveafuck</a><br>
<a href="/r/tipofmytongue" rel="nofollow">/r/tipofmytongue</a><br>
<a href="/r/quotes" rel="nofollow">/r/quotes</a><br>
<a href="/r/casualconversation" rel="nofollow">/r/casualconversation</a> </p>
<h2 id="wiki_advice"><strong>Advice</strong></h2>
<p>For more advice/assistance subreddits, <a href="http://www.reddit.com/r/ListOfSubreddits/wiki/advice" rel="nofollow">see here!</a></p>
<p><a href="/r/relationship_advice" rel="nofollow">/r/relationship_advice</a><br>
<a href="/r/raisedbynarcissists" rel="nofollow">/r/raisedbynarcissists</a><br>
<a href="/r/legaladvice" rel="nofollow">/r/legaladvice</a> and <a href="/r/bestoflegaladvice" rel="nofollow">/r/bestoflegaladvice</a><br>
<a href="/r/advice" rel="nofollow">/r/advice</a> </p>
<h2 id="wiki_ama"><strong>AMA</strong></h2>
<p><a href="/r/IAmA" rel="nofollow">/r/IAmA</a><br>
<a href="/r/ExplainlikeIAmA" rel="nofollow">/r/ExplainlikeIAmA</a><br>
<a href="/r/AMA" rel="nofollow">/r/AMA</a><br>
<a href="/r/casualiama" rel="nofollow">/r/casualiama</a><br>
<a href="/r/de_Iama" rel="nofollow">/r/de_Iama</a> </p>
<h2 id="wiki_games"><strong>Games</strong></h2>
<p><a href="/r/whowouldwin" rel="nofollow">/r/whowouldwin</a><br>
<a href="/r/wouldyourather" rel="nofollow">/r/wouldyourather</a><br>
<a href="/r/scenesfromahat" rel="nofollow">/r/scenesfromahat</a><br>
<a href="/r/AskOuija" rel="nofollow">/r/AskOuija</a> </p>
<h2 id="wiki_question.2Fanswer"><strong>Question/Answer</strong></h2>
<p><a href="/r/whatisthisthing" rel="nofollow">/r/whatisthisthing</a>   For more like this, see <a href="http://www.reddit.com/user/AskReddit_Multis/m/what_is_this___" rel="nofollow">here</a> from <a href="/r/AskReddit" rel="nofollow">/r/AskReddit</a>!<br>
<a href="/r/answers" rel="nofollow">/r/answers</a><br>
<a href="/r/NoStupidQuestions" rel="nofollow">/r/NoStupidQuestions</a><br>
<a href="/r/amiugly" rel="nofollow">/r/amiugly</a><br>
<a href="/r/whatsthisbug" rel="nofollow">/r/whatsthisbug</a><br>
<a href="/r/samplesize" rel="nofollow">/r/samplesize</a><br>
<a href="/r/tooafraidtoask" rel="nofollow">/r/tooafraidtoask</a><br>
<a href="/r/whatsthisplant" rel="nofollow">/r/whatsthisplant</a> </p>
<h3 id="wiki_ask______"><em>Ask______</em></h3>
<p><strong><a href="/r/AskReddit" rel="nofollow">/r/AskReddit</a></strong><br>
<a href="/r/ShittyAskScience" rel="nofollow">/r/ShittyAskScience</a><br>
<a href="/r/TrueAskReddit" rel="nofollow">/r/TrueAskReddit</a><br>
<a href="/r/AskScienceFiction" rel="nofollow">/r/AskScienceFiction</a><br>
<a href="/r/AskOuija" rel="nofollow">/r/AskOuija</a> </p>
<h4 id="wiki_occupation"><em>Occupation</em></h4>
<p><strong><a href="/r/AskScience" rel="nofollow">/r/AskScience</a></strong><br>
<a href="/r/askhistorians" rel="nofollow">/r/askhistorians</a><br>
<a href="/r/askculinary" rel="nofollow">/r/askculinary</a><br>
<a href="/r/AskSocialScience" rel="nofollow">/r/AskSocialScience</a><br>
<a href="/r/askengineers" rel="nofollow">/r/askengineers</a><br>
<a href="/r/askphilosophy" rel="nofollow">/r/askphilosophy</a> </p>
<h4 id="wiki_sex.2Fgender"><em>Sex/Gender</em></h4>
<p><a href="/r/askwomen" rel="nofollow">/r/askwomen</a><br>
<a href="/r/askmen" rel="nofollow">/r/askmen</a><br>
<a href="/r/askgaybros" rel="nofollow">/r/askgaybros</a><br>
<a href="/r/askredditafterdark" rel="nofollow">/r/askredditafterdark</a><br>
<a href="/r/asktransgender" rel="nofollow">/r/asktransgender</a> </p>
<h2 id="wiki_stories"><strong>Stories</strong></h2>
<p><a href="/r/tifu" rel="nofollow">/r/tifu</a><br>
<a href="/r/self" rel="nofollow">/r/self</a><br>
<a href="/r/confession" rel="nofollow">/r/confession</a><br>
<a href="/r/fatpeoplestories" rel="nofollow">/r/fatpeoplestories</a><br>
<a href="/r/confessions" rel="nofollow">/r/confessions</a> </p>
<h3 id="wiki_customer_service"><em>Customer Service</em></h3>
<p><a href="/r/talesfromtechsupport" rel="nofollow">/r/talesfromtechsupport</a><br>
<a href="/r/talesfromretail" rel="nofollow">/r/talesfromretail</a><br>
<a href="/r/techsupportmacgyver" rel="nofollow">/r/techsupportmacgyver</a><br>
<a href="/r/idontworkherelady" rel="nofollow">/r/idontworkherelady</a><br>
<a href="/r/TalesFromYourServer" rel="nofollow">/r/TalesFromYourServer</a><br>
<a href="/r/KitchenConfidential" rel="nofollow">/r/KitchenConfidential</a><br>
<a href="/r/TalesFromThePizzaGuy" rel="nofollow">/r/TalesFromThePizzaGuy</a><br>
<a href="/r/TalesFromTheFrontDesk" rel="nofollow">/r/TalesFromTheFrontDesk</a><br>
<a href="/r/talesfromthecustomer" rel="nofollow">/r/talesfromthecustomer</a><br>
<a href="/r/talesfromcallcenters" rel="nofollow">/r/talesfromcallcenters</a><br>
<a href="/r/talesfromthesquadcar" rel="nofollow">/r/talesfromthesquadcar</a><br>
<a href="/r/talesfromthepharmacy" rel="nofollow">/r/talesfromthepharmacy</a><br>
<a href="/r/starbucks" rel="nofollow">/r/starbucks</a> </p>
<h3 id="wiki_revenge"><em>Revenge</em></h3>
<p><a href="/r/pettyrevenge" rel="nofollow">/r/pettyrevenge</a><br>
<a href="/r/prorevenge" rel="nofollow">/r/prorevenge</a> </p>
<h3 id="wiki_scary.2Fweird"><em>Scary/Weird</em></h3>
<p><a href="/r/nosleep" rel="nofollow">/r/nosleep</a><br>
<a href="/r/LetsNotMeet" rel="nofollow">/r/LetsNotMeet</a><br>
<a href="/r/Glitch_in_the_Matrix" rel="nofollow">/r/Glitch_in_the_Matrix</a><br>
<a href="/r/shortscarystories" rel="nofollow">/r/shortscarystories</a><br>
<a href="/r/thetruthishere" rel="nofollow">/r/thetruthishere</a><br>
<a href="/r/UnresolvedMysteries" rel="nofollow">/r/UnresolvedMysteries</a><br>
<a href="/r/UnsolvedMysteries" rel="nofollow">/r/UnsolvedMysteries</a> </p>
<h2 id="wiki_support"><strong>Support</strong></h2>
<p><a href="/r/depression" rel="nofollow">/r/depression</a><br>
<a href="/r/SuicideWatch" rel="nofollow">/r/SuicideWatch</a><br>
<a href="/r/Anxiety" rel="nofollow">/r/Anxiety</a><br>
<a href="/r/foreveralone" rel="nofollow">/r/foreveralone</a><br>
<a href="/r/offmychest" rel="nofollow">/r/offmychest</a><br>
<a href="/r/socialanxiety" rel="nofollow">/r/socialanxiety</a><br>
<a href="/r/trueoffmychest" rel="nofollow">/r/trueoffmychest</a> </p>
<hr>
<h1 id="wiki_educational"><strong>Educational</strong></h1>
<h2 id="wiki_general2">General</h2>
<p><a href="/r/YouShouldKnow" rel="nofollow">/r/YouShouldKnow</a><br>
<a href="/r/everymanshouldknow" rel="nofollow">/r/everymanshouldknow</a><br>
<a href="/r/LearnUselessTalents" rel="nofollow">/r/LearnUselessTalents</a><br>
<a href="/r/changemyview" rel="nofollow">/r/changemyview</a><br>
<a href="/r/howto" rel="nofollow">/r/howto</a><br>
<a href="/r/Foodforthought" rel="nofollow">/r/Foodforthought</a><br>
<a href="/r/educationalgifs" rel="nofollow">/r/educationalgifs</a><br>
<a href="/r/lectures" rel="nofollow">/r/lectures</a><br>
<a href="/r/education" rel="nofollow">/r/education</a><br>
<a href="/r/college" rel="nofollow">/r/college</a><br>
<a href="/r/GetStudying" rel="nofollow">/r/GetStudying</a><br>
<a href="/r/teachers" rel="nofollow">/r/teachers</a><br>
<a href="/r/watchandlearn" rel="nofollow">/r/watchandlearn</a><br>
<a href="/r/bulletjournal" rel="nofollow">/r/bulletjournal</a><br>
<a href="/r/applyingtocollege" rel="nofollow">/r/applyingtocollege</a><br>
<a href="/r/lawschool" rel="nofollow">/r/lawschool</a> </p>
<h3 id="wiki_facts"><em>Facts</em></h3>
<p><a href="/r/todayilearned" rel="nofollow">/r/todayilearned</a><br>
<a href="/r/wikipedia" rel="nofollow">/r/wikipedia</a> </p>
<h3 id="wiki_questions"><em>Questions</em></h3>
<p><a href="/r/OutOfTheLoop" rel="nofollow">/r/OutOfTheLoop</a><br>
<a href="/r/IWantToLearn" rel="nofollow">/r/IWantToLearn</a> </p>
<h4 id="wiki_explain_like..."><em>Explain Like...</em></h4>
<p><strong><a href="/r/explainlikeimfive" rel="nofollow">/r/explainlikeimfive</a></strong><br>
<a href="/r/explainlikeIAmA" rel="nofollow">/r/explainlikeIAmA</a><br>
<a href="/r/ExplainLikeImCalvin" rel="nofollow">/r/ExplainLikeImCalvin</a> </p>
<h2 id="wiki_anthropology"><strong>Anthropology</strong></h2>
<p><a href="/r/anthropology" rel="nofollow">/r/anthropology</a> </p>
<h2 id="wiki_art"><strong>Art</strong></h2>
<p><a href="/r/Art" rel="nofollow">/r/Art</a> (For more art related subreddits, <a href="http://www.reddit.com/r/Art/wiki/related" rel="nofollow">click here!</a>)<br>
<a href="/r/redditgetsdrawn" rel="nofollow">/r/redditgetsdrawn</a><br>
<a href="/r/heavymind" rel="nofollow">/r/heavymind</a><br>
<a href="/r/drawing" rel="nofollow">/r/drawing</a><br>
<a href="/r/graffiti" rel="nofollow">/r/graffiti</a><br>
<a href="/r/retrofuturism" rel="nofollow">/r/retrofuturism</a><br>
<a href="/r/sketchdaily" rel="nofollow">/r/sketchdaily</a><br>
<a href="/r/ArtPorn" rel="nofollow">/r/ArtPorn</a><br>
<a href="/r/pixelart" rel="nofollow">/r/pixelart</a><br>
<a href="/r/artfundamentals" rel="nofollow">/r/artfundamentals</a><br>
<a href="/r/learnart" rel="nofollow">/r/learnart</a><br>
<a href="/r/specart" rel="nofollow">/r/specart</a><br>
<a href="/r/breadstapledtotrees" rel="nofollow">/r/breadstapledtotrees</a><br>
<a href="/r/animation" rel="nofollow">/r/animation</a><br>
<a href="/r/wimmelbilder" rel="nofollow">/r/wimmelbilder</a><br>
<a href="/r/illustration" rel="nofollow">/r/illustration</a><br>
<a href="/r/streetart" rel="nofollow">/r/streetart</a> </p>
<h3 id="wiki_painting"><em>Painting</em></h3>
<p><a href="/r/painting" rel="nofollow">/r/painting</a><br>
<a href="/r/minipainting" rel="nofollow">/r/minipainting</a> </p>
<h2 id="wiki_computer_science.2Fengineering"><strong>Computer Science/Engineering</strong></h2>
<p><a href="/r/gamedev" rel="nofollow">/r/gamedev</a><br>
<a href="/r/engineering" rel="nofollow">/r/engineering</a><br>
<a href="/r/ubuntu" rel="nofollow">/r/ubuntu</a><br>
<a href="/r/cscareerquestions" rel="nofollow">/r/cscareerquestions</a><br>
<a href="/r/EngineeringStudents" rel="nofollow">/r/EngineeringStudents</a><br>
<a href="/r/askengineers" rel="nofollow">/r/askengineers</a> </p>
<h3 id="wiki_coding"><em>Coding</em></h3>
<p><a href="/r/learnprogramming" rel="nofollow">/r/learnprogramming</a><br>
<a href="/r/compsci" rel="nofollow">/r/compsci</a><br>
<a href="/r/java" rel="nofollow">/r/java</a><br>
<a href="/r/javascript" rel="nofollow">/r/javascript</a><br>
<a href="/r/coding" rel="nofollow">/r/coding</a><br>
<a href="/r/machinelearning" rel="nofollow">/r/machinelearning</a><br>
<a href="/r/howtohack" rel="nofollow">/r/howtohack</a><br>
<a href="/r/cpp" rel="nofollow">/r/cpp</a><br>
<a href="/r/artificial" rel="nofollow">/r/artificial</a> </p>
<h4 id="wiki_python"><em>Python</em></h4>
<p><a href="/r/python" rel="nofollow">/r/python</a><br>
<a href="/r/learnpython" rel="nofollow">/r/learnpython</a> </p>
<h2 id="wiki_economics"><strong>Economics</strong></h2>
<p><a href="/r/Economics" rel="nofollow">/r/Economics</a><br>
<a href="/r/business" rel="nofollow">/r/business</a><br>
<a href="/r/entrepreneur" rel="nofollow">/r/entrepreneur</a><br>
<a href="/r/marketing" rel="nofollow">/r/marketing</a><br>
<a href="/r/BasicIncome" rel="nofollow">/r/BasicIncome</a> </p>
<h3 id="wiki_business"><em>Business</em></h3>
<p><a href="/r/business" rel="nofollow">/r/business</a><br>
<a href="/r/smallbusiness" rel="nofollow">/r/smallbusiness</a> </p>
<h3 id="wiki_stocks"><em>Stocks</em></h3>
<p><a href="/r/stocks" rel="nofollow">/r/stocks</a><br>
<a href="/r/wallstreetbets" rel="nofollow">/r/wallstreetbets</a><br>
<a href="/r/stockmarket" rel="nofollow">/r/stockmarket</a> </p>
<h2 id="wiki_environment"><strong>Environment</strong></h2>
<p><a href="/r/environment" rel="nofollow">/r/environment</a><br>
<a href="/r/zerowaste" rel="nofollow">/r/zerowaste</a> </p>
<h2 id="wiki_history"><strong>History</strong></h2>
<p>For more, see <a href="http://www.reddit.com/r/HistoryNetwork/wiki/listofhistorysubreddits" rel="nofollow">the wiki compiled</a> by <a href="/r/historynetwork" rel="nofollow">/r/historynetwork</a>!<br>
Note: Many of those subreddits are inactive.</p>
<p><a href="/r/history" rel="nofollow">/r/history</a><br>
<a href="/r/AskHistorians" rel="nofollow">/r/AskHistorians</a><br>
<a href="/r/ColorizedHistory" rel="nofollow">/r/ColorizedHistory</a><br>
<a href="/r/badhistory" rel="nofollow">/r/badhistory</a><br>
<a href="/r/100yearsago" rel="nofollow">/r/100yearsago</a> </p>
<h3 id="wiki_historical_images"><em>Historical Images</em></h3>
<p><a href="/r/HistoryPorn" rel="nofollow">/r/HistoryPorn</a><br>
<a href="/r/PropagandaPosters" rel="nofollow">/r/PropagandaPosters</a><br>
<a href="/r/TheWayWeWere" rel="nofollow">/r/TheWayWeWere</a><br>
<a href="/r/historymemes" rel="nofollow">/r/historymemes</a><br>
<a href="/r/castles" rel="nofollow">/r/castles</a> </p>
<h2 id="wiki_language"><strong>Language</strong></h2>
<p><a href="/r/linguistics" rel="nofollow">/r/linguistics</a><br>
<a href="/r/languagelearning" rel="nofollow">/r/languagelearning</a><br>
<a href="/r/learnjapanese" rel="nofollow">/r/learnjapanese</a><br>
<a href="/r/french" rel="nofollow">/r/french</a> </p>
<h2 id="wiki_law"><strong>Law</strong></h2>
<p><a href="/r/law" rel="nofollow">/r/law</a> </p>
<h2 id="wiki_math"><strong>Math</strong></h2>
<p><a href="/r/math" rel="nofollow">/r/math</a><br>
<a href="/r/theydidthemath" rel="nofollow">/r/theydidthemath</a> </p>
<h2 id="wiki_medicine"><strong>Medicine</strong></h2>
<p><a href="/r/medicalschool" rel="nofollow">/r/medicalschool</a> </p>
<h2 id="wiki_psychology"><strong>Psychology</strong></h2>
<p><a href="/r/psychology" rel="nofollow">/r/psychology</a>
<a href="/r/JordanPeterson" rel="nofollow">/r/JordanPeterson</a> </p>
<h2 id="wiki_science2"><strong>Science</strong></h2>
<p><a href="/r/Science" rel="nofollow">/r/Science</a><br>
<strong><a href="/r/AskScience" rel="nofollow">/r/AskScience</a></strong><br>
<a href="/r/cogsci" rel="nofollow">/r/cogsci</a><br>
<a href="/r/medicine" rel="nofollow">/r/medicine</a><br>
<a href="/r/everythingscience" rel="nofollow">/r/everythingscience</a><br>
<a href="/r/geology" rel="nofollow">/r/geology</a> </p>
<h3 id="wiki_astronomy"><em>Astronomy</em></h3>
<p><strong><a href="/r/Space" rel="nofollow">/r/Space</a></strong><br>
<a href="/r/SpacePorn" rel="nofollow">/r/SpacePorn</a><br>
<a href="/r/astronomy" rel="nofollow">/r/astronomy</a><br>
<a href="/r/astrophotography" rel="nofollow">/r/astrophotography</a><br>
<a href="/r/spacex" rel="nofollow">/r/spacex</a><br>
<a href="/r/nasa" rel="nofollow">/r/nasa</a> </p>
<h3 id="wiki_biology"><em>Biology</em></h3>
<p><a href="/r/biology" rel="nofollow">/r/biology</a><br>
<a href="/r/Awwducational" rel="nofollow">/r/Awwducational</a> </p>
<h3 id="wiki_chemistry"><em>Chemistry</em></h3>
<p><a href="/r/chemicalreactiongifs" rel="nofollow">/r/chemicalreactiongifs</a><br>
<a href="/r/chemistry" rel="nofollow">/r/chemistry</a> </p>
<h3 id="wiki_physics"><em>Physics</em></h3>
<p><a href="/r/physics" rel="nofollow">/r/physics</a> </p>
<hr>
<h1 id="wiki_entertainment"><strong>Entertainment</strong></h1>
<h2 id="wiki_general3"><strong>General</strong></h2>
<p><a href="/r/entertainment" rel="nofollow">/r/entertainment</a><br>
<a href="/r/fantheories" rel="nofollow">/r/fantheories</a><br>
<a href="/r/Disney" rel="nofollow">/r/Disney</a><br>
<a href="/r/obscuremedia" rel="nofollow">/r/obscuremedia</a> </p>
<h2 id="wiki_anime.2Fmanga"><strong>Anime/Manga</strong></h2>
<p><a href="/r/anime" rel="nofollow">/r/anime</a><br>
<a href="/r/manga" rel="nofollow">/r/manga</a><br>
<a href="/r/anime_irl" rel="nofollow">/r/anime_irl</a><br>
<a href="/r/awwnime" rel="nofollow">/r/awwnime</a><br>
<a href="/r/TsundereSharks" rel="nofollow">/r/TsundereSharks</a><br>
<a href="/r/animesuggest" rel="nofollow">/r/animesuggest</a><br>
<a href="/r/animemes" rel="nofollow">/r/animemes</a><br>
<a href="/r/animegifs" rel="nofollow">/r/animegifs</a><br>
<a href="/r/animewallpaper" rel="nofollow">/r/animewallpaper</a> </p>
<h3 id="wiki_individual_anime.2Fmanga"><em>Individual Anime/manga</em></h3>
<p><a href="/r/pokemon" rel="nofollow">/r/pokemon</a><br>
<a href="/r/onepiece" rel="nofollow">/r/onepiece</a><br>
<a href="/r/naruto" rel="nofollow">/r/naruto</a><br>
<a href="/r/dbz" rel="nofollow">/r/dbz</a><br>
<a href="/r/onepunchman" rel="nofollow">/r/onepunchman</a><br>
<a href="/r/ShingekiNoKyojin" rel="nofollow">/r/ShingekiNoKyojin</a><br>
<a href="/r/yugioh" rel="nofollow">/r/yugioh</a><br>
<a href="/r/BokuNoHeroAcademia" rel="nofollow">/r/BokuNoHeroAcademia</a><br>
<a href="/r/DDLC" rel="nofollow">/r/DDLC</a><br>
<a href="/r/berserk" rel="nofollow">/r/berserk</a><br>
<a href="/r/hunterxhunter" rel="nofollow">/r/hunterxhunter</a><br>
<a href="/r/tokyoghoul" rel="nofollow">/r/tokyoghoul</a> </p>
<h2 id="wiki_books.2Fwriting"><strong>Books/Writing</strong></h2>
<p><a href="/r/Books" rel="nofollow">/r/Books</a><br>
<a href="/r/WritingPrompts" rel="nofollow">/r/WritingPrompts</a><br>
<a href="/r/writing" rel="nofollow">/r/writing</a><br>
<a href="/r/literature" rel="nofollow">/r/literature</a><br>
<a href="/r/booksuggestions" rel="nofollow">/r/booksuggestions</a><br>
<a href="/r/lifeofnorman" rel="nofollow">/r/lifeofnorman</a><br>
<a href="/r/poetry" rel="nofollow">/r/poetry</a><br>
<a href="/r/screenwriting" rel="nofollow">/r/screenwriting</a><br>
<a href="/r/freeEbooks" rel="nofollow">/r/freeEbooks</a><br>
<a href="/r/boottoobig" rel="nofollow">/r/boottoobig</a><br>
<a href="/r/hfy" rel="nofollow">/r/hfy</a><br>
<a href="/r/suggestmeabook" rel="nofollow">/r/suggestmeabook</a><br>
<a href="/r/lovecraft" rel="nofollow">/r/lovecraft</a> </p>
<h3 id="wiki_comics"><em>Comics</em></h3>
<p><a href="/r/comics" rel="nofollow">/r/comics</a><br>
<a href="/r/comicbooks" rel="nofollow">/r/comicbooks</a><br>
<a href="/r/polandball" rel="nofollow">/r/polandball</a><br>
<a href="/r/marvel" rel="nofollow">/r/marvel</a><br>
<a href="/r/webcomics" rel="nofollow">/r/webcomics</a><br>
<a href="/r/bertstrips" rel="nofollow">/r/bertstrips</a><br>
<a href="/r/marvelstudios" rel="nofollow">/r/marvelstudios</a><br>
<a href="/r/defenders" rel="nofollow">/r/defenders</a> </p>
<h3 id="wiki_individual_books.2Fstories.2Fcomics"><em>Individual books/stories/comics</em></h3>
<p><a href="/r/harrypotter" rel="nofollow">/r/harrypotter</a><br>
<a href="/r/batman" rel="nofollow">/r/batman</a><br>
<a href="/r/calvinandhobbes" rel="nofollow">/r/calvinandhobbes</a> (and <a href="/r/explainlikeimcalvin" rel="nofollow">/r/explainlikeimcalvin</a>)<br>
<a href="/r/xkcd" rel="nofollow">/r/xkcd</a><br>
<a href="/r/DCComics" rel="nofollow">/r/DCComics</a><br>
<a href="/r/arrow" rel="nofollow">/r/arrow</a><br>
<a href="/r/unexpectedhogwarts" rel="nofollow">/r/unexpectedhogwarts</a><br>
<a href="/r/spiderman" rel="nofollow">/r/spiderman</a><br>
<a href="/r/deadpool" rel="nofollow">/r/deadpool</a><br>
<a href="/r/KingkillerChronicle" rel="nofollow">/r/KingkillerChronicle</a> </p>
<h4 id="wiki_game_of_thrones"><em>Game of Thrones</em></h4>
<p><a href="/r/asoiaf" rel="nofollow">/r/asoiaf</a><br>
<a href="/r/gameofthrones" rel="nofollow">/r/gameofthrones</a><br>
<a href="/r/freefolk" rel="nofollow">/r/freefolk</a> </p>
<h4 id="wiki_lord_of_the_rings"><em>Lord of the Rings</em></h4>
<p><a href="/r/lotr" rel="nofollow">/r/lotr</a><br>
<a href="/r/lotrmemes" rel="nofollow">/r/lotrmemes</a><br>
<a href="/r/tolkeinfans" rel="nofollow">/r/tolkeinfans</a> </p>
<h2 id="wiki_celebrities"><strong>Celebrities</strong></h2>
<p><a href="/r/celebs" rel="nofollow">/r/celebs</a><br>
<a href="/r/celebhub" rel="nofollow">/r/celebhub</a> </p>
<h3 id="wiki_individual_celebrities"><em>Individual Celebrities</em></h3>
<h4 id="wiki_female"><em>Female</em></h4>
<p><a href="/r/EmmaWatson" rel="nofollow">/r/EmmaWatson</a><br>
<a href="/r/jessicanigri" rel="nofollow">/r/jessicanigri</a><br>
<a href="/r/kateupton" rel="nofollow">/r/kateupton</a><br>
<a href="/r/alisonbrie" rel="nofollow">/r/alisonbrie</a><br>
<a href="/r/EmilyRatajkowski" rel="nofollow">/r/EmilyRatajkowski</a><br>
<a href="/r/jenniferlawrence" rel="nofollow">/r/jenniferlawrence</a><br>
<a href="/r/alexandradaddario" rel="nofollow">/r/alexandradaddario</a> </p>
<h4 id="wiki_male"><em>Male</em></h4>
<p><a href="/r/onetruegod" rel="nofollow">/r/onetruegod</a><br>
<a href="/r/joerogan" rel="nofollow">/r/joerogan</a><br>
<a href="/r/keanubeingawesome" rel="nofollow">/r/keanubeingawesome</a><br>
<a href="/r/crewscrew" rel="nofollow">/r/crewscrew</a><br>
<a href="/r/donaldglover" rel="nofollow">/r/donaldglover</a><br>
<a href="/r/elonmusk" rel="nofollow">/r/elonmusk</a> </p>
<h2 id="wiki_cosplay"><strong>Cosplay</strong></h2>
<p><a href="/r/cosplay" rel="nofollow">/r/cosplay</a><br>
<a href="/r/cosplaygirls" rel="nofollow">/r/cosplaygirls</a> </p>
<h2 id="wiki_games2"><strong>Games</strong></h2>
<p><a href="/r/lego" rel="nofollow">/r/lego</a><br>
<a href="/r/boardgames" rel="nofollow">/r/boardgames</a><br>
<a href="/r/rpg" rel="nofollow">/r/rpg</a><br>
<a href="/r/chess" rel="nofollow">/r/chess</a><br>
<a href="/r/poker" rel="nofollow">/r/poker</a><br>
<a href="/r/jrpg" rel="nofollow">/r/jrpg</a> </p>
<h3 id="wiki_dungeons_and_dragons"><em>Dungeons and Dragons</em></h3>
<p><a href="/r/DnD" rel="nofollow">/r/DnD</a><br>
<a href="/r/DnDGreentext" rel="nofollow">/r/DnDGreentext</a><br>
<a href="/r/DnDBehindTheScreen" rel="nofollow">/r/DnDBehindTheScreen</a><br>
<a href="/r/dndnext" rel="nofollow">/r/dndnext</a><br>
<a href="/r/dungeonsanddragons" rel="nofollow">/r/dungeonsanddragons</a><br>
<a href="/r/criticalrole" rel="nofollow">/r/criticalrole</a><br>
<a href="/r/DMAcademy" rel="nofollow">/r/DMAcademy</a> </p>
<h3 id="wiki_magic"><em>Magic</em></h3>
<p><a href="/r/magicTCG" rel="nofollow">/r/magicTCG</a><br>
<a href="/r/modernmagic" rel="nofollow">/r/modernmagic</a> </p>
<h2 id="wiki_video_games"><a href="https://www.reddit.com/r/ListOfSubreddits/wiki/games50k" rel="nofollow"><strong>Video games</strong></a></h2>
<p><em>The above is the complete list of every video game subreddit with currently 50k or more subscribers!</em></p>
<h2 id="wiki_genres"><strong>Genres</strong></h2>
<p><a href="/r/zombies" rel="nofollow">/r/zombies</a><br>
<a href="/r/cyberpunk" rel="nofollow">/r/cyberpunk</a> </p>
<h3 id="wiki_fantasy"><em>Fantasy</em></h3>
<p><a href="/r/fantasy" rel="nofollow">/r/fantasy</a> </p>
<h3 id="wiki_sci-fi"><em>Sci-fi</em></h3>
<p><a href="https://www.reddit.com/r/SpaceGeek/wiki/relatedsubreddits" rel="nofollow">For other sci-fi subreddits, see here!</a></p>
<p><a href="/r/scifi" rel="nofollow">/r/scifi</a><br>
<a href="/r/starwars" rel="nofollow">/r/starwars</a><br>
<a href="/r/startrek" rel="nofollow">/r/startrek</a><br>
<a href="/r/asksciencefiction" rel="nofollow">/r/asksciencefiction</a><br>
<a href="/r/prequelmemes" rel="nofollow">/r/prequelmemes</a><br>
<a href="/r/empiredidnothingwrong" rel="nofollow">/r/empiredidnothingwrong</a><br>
<a href="/r/SequelMemes" rel="nofollow">/r/SequelMemes</a><br>
<a href="/r/sciencefiction" rel="nofollow">/r/sciencefiction</a> </p>
<h2 id="wiki_internet.2Fapps"><strong>Internet/Apps</strong></h2>
<p><strong><a href="/r/InternetIsBeautiful" rel="nofollow">/r/InternetIsBeautiful</a></strong><br>
<a href="/r/facepalm" rel="nofollow">/r/facepalm</a><br>
<a href="/r/wikipedia" rel="nofollow">/r/wikipedia</a><br>
<a href="/r/creepyPMs" rel="nofollow">/r/creepyPMs</a><br>
<a href="/r/web_design" rel="nofollow">/r/web_design</a><br>
<a href="/r/google" rel="nofollow">/r/google</a><br>
<a href="/r/KenM" rel="nofollow">/r/KenM</a><br>
<a href="/r/bannedfromclubpenguin" rel="nofollow">/r/bannedfromclubpenguin</a><br>
<a href="/r/savedyouaclick" rel="nofollow">/r/savedyouaclick</a><br>
<a href="/r/bestofworldstar" rel="nofollow">/r/bestofworldstar</a><br>
<a href="/r/discordapp" rel="nofollow">/r/discordapp</a><br>
<a href="/r/snaplenses" rel="nofollow">/r/snaplenses</a><br>
<a href="/r/tronix" rel="nofollow">/r/tronix</a> </p>
<h3 id="wiki_4chan"><em>4chan</em></h3>
<p><a href="/r/4chan" rel="nofollow">/r/4chan</a><br>
<a href="/r/Classic4chan" rel="nofollow">/r/Classic4chan</a><br>
<a href="/r/greentext" rel="nofollow">/r/greentext</a> </p>
<h3 id="wiki_facebook"><em>Facebook</em></h3>
<p><a href="/r/facepalm" rel="nofollow">/r/facepalm</a><br>
<a href="/r/oldpeoplefacebook" rel="nofollow">/r/oldpeoplefacebook</a><br>
<a href="/r/facebookwins" rel="nofollow">/r/facebookwins</a><br>
<a href="/r/indianpeoplefacebook" rel="nofollow">/r/indianpeoplefacebook</a><br>
<a href="/r/terriblefacebookmemes" rel="nofollow">/r/terriblefacebookmemes</a><br>
<a href="/r/insanepeoplefacebook" rel="nofollow">/r/insanepeoplefacebook</a> </p>
<h3 id="wiki_internet_dating"><em>Internet Dating</em></h3>
<p><a href="/r/Tinder" rel="nofollow">/r/Tinder</a><br>
<a href="/r/OkCupid" rel="nofollow">/r/OkCupid</a> </p>
<h3 id="wiki_internet_politics"><em>Internet Politics</em></h3>
<p><a href="/r/KotakuInAction" rel="nofollow">/r/KotakuInAction</a><br>
<a href="/r/wikileaks" rel="nofollow">/r/wikileaks</a><br>
<a href="/r/shitcosmosays" rel="nofollow">/r/shitcosmosays</a> </p>
<h3 id="wiki_live_streaming"><em>Live Streaming</em></h3>
<p><a href="/r/twitch" rel="nofollow">/r/twitch</a><br>
<a href="/r/livestreamfail" rel="nofollow">/r/livestreamfail</a> </p>
<h3 id="wiki_podcasts"><em>Podcasts</em></h3>
<p><a href="/r/serialpodcast" rel="nofollow">/r/serialpodcast</a><br>
<a href="/r/podcasts" rel="nofollow">/r/podcasts</a> </p>
<h3 id="wiki_tumblr"><em>Tumblr</em></h3>
<p><a href="/r/tumblrinaction" rel="nofollow">/r/tumblrinaction</a><br>
<a href="/r/tumblr" rel="nofollow">/r/tumblr</a> </p>
<h3 id="wiki_twitter"><em>Twitter</em></h3>
<p><a href="/r/blackpeopletwitter" rel="nofollow">/r/blackpeopletwitter</a><br>
<a href="/r/scottishpeopletwitter" rel="nofollow">/r/scottishpeopletwitter</a><br>
<a href="/r/WhitePeopleTwitter" rel="nofollow">/r/WhitePeopleTwitter</a><br>
<a href="/r/wholesomebpt" rel="nofollow">/r/wholesomebpt</a><br>
<a href="/r/latinopeopletwitter" rel="nofollow">/r/latinopeopletwitter</a> </p>
<h3 id="wiki_youtube"><em>YouTube</em></h3>
<p><a href="/r/YoutubeHaiku" rel="nofollow">/r/YoutubeHaiku</a><br>
<a href="/r/youtube" rel="nofollow">/r/youtube</a> </p>
<h4 id="wiki_individual_youtubers.2Fcompanies"><em>Individual YouTubers/Companies</em></h4>
<p><a href="/r/gamegrumps" rel="nofollow">/r/gamegrumps</a><br>
<a href="/r/h3h3productions" rel="nofollow">/r/h3h3productions</a><br>
<a href="/r/CGPGrey" rel="nofollow">/r/CGPGrey</a><br>
<a href="/r/yogscast" rel="nofollow">/r/yogscast</a><br>
<a href="/r/jontron" rel="nofollow">/r/jontron</a><br>
<a href="/r/Idubbbz" rel="nofollow">/r/Idubbbz</a><br>
<a href="/r/defranco" rel="nofollow">/r/defranco</a><br>
<a href="/r/cynicalbrit" rel="nofollow">/r/cynicalbrit</a><br>
<a href="/r/pewdiepiesubmissions" rel="nofollow">/r/pewdiepiesubmissions</a><br>
<a href="/r/pyrocynical" rel="nofollow">/r/pyrocynical</a><br>
<a href="/r/SovietWomble" rel="nofollow">/r/SovietWomble</a><br>
<a href="/r/RedLetterMedia" rel="nofollow">/r/RedLetterMedia</a><br>
<a href="/r/videogamedunkey" rel="nofollow">/r/videogamedunkey</a><br>
<a href="/r/loltyler1" rel="nofollow">/r/loltyler1</a> </p>
<h5 id="wiki_roosterteeth"><em>Roosterteeth</em></h5>
<p><a href="/r/roosterteeth" rel="nofollow">/r/roosterteeth</a><br>
<a href="/r/funhaus" rel="nofollow">/r/funhaus</a><br>
<a href="/r/rwby" rel="nofollow">/r/rwby</a><br>
<a href="/r/cowchop" rel="nofollow">/r/cowchop</a> </p>
<h2 id="wiki_movies"><strong>Movies</strong></h2>
<p><a href="/r/movies" rel="nofollow">/r/movies</a><br>
<a href="/r/documentaries" rel="nofollow">/r/documentaries</a><br>
<a href="/r/fullmoviesonyoutube" rel="nofollow">/r/fullmoviesonyoutube</a><br>
<a href="/r/truefilm" rel="nofollow">/r/truefilm</a><br>
<a href="/r/bollywoodrealism" rel="nofollow">/r/bollywoodrealism</a><br>
<a href="/r/moviedetails" rel="nofollow">/r/moviedetails</a><br>
<a href="/r/moviesinthemaking" rel="nofollow">/r/moviesinthemaking</a><br>
<a href="/r/fullmoviesonvimeo" rel="nofollow">/r/fullmoviesonvimeo</a><br>
<a href="/r/continuityporn" rel="nofollow">/r/continuityporn</a><br>
<a href="/r/ghibli" rel="nofollow">/r/ghibli</a><br>
<a href="/r/cinematography" rel="nofollow">/r/cinematography</a><br>
<a href="/r/shittymoviedetails" rel="nofollow">/r/shittymoviedetails</a> </p>
<h3 id="wiki_individual_movies.2Fseries"><em>Individual Movies/Series</em></h3>
<p><a href="/r/starwars" rel="nofollow">/r/starwars</a><br>
<a href="/r/harrypotter" rel="nofollow">/r/harrypotter</a><br>
<a href="/r/lotr" rel="nofollow">/r/lotr</a><br>
<a href="/r/lotrmemes" rel="nofollow">/r/lotrmemes</a><br>
<a href="/r/otmemes" rel="nofollow">/r/otmemes</a> </p>
<h4 id="wiki_comic_movies"><em>Comic movies</em></h4>
<p><a href="/r/marvelstudios" rel="nofollow">/r/marvelstudios</a><br>
<a href="/r/batman" rel="nofollow">/r/batman</a><br>
<a href="/r/DC_Cinematic" rel="nofollow">/r/DC_Cinematic</a><br>
<a href="/r/thanosdidnothingwrong" rel="nofollow">/r/thanosdidnothingwrong</a><br>
<a href="/r/intothesoulstone" rel="nofollow">/r/intothesoulstone</a> </p>
<h2 id="wiki_music"><strong>Music</strong></h2>
<p>Much more [here](<a href="http://www.reddit.com/r/listentothis/about/sidebar%5C" rel="nofollow">http://www.reddit.com/r/listentothis/about/sidebar\</a>) from the sidebar of <a href="/r/listentothis" rel="nofollow">/r/listentothis</a>!<br>
See especially [The Fire Hose](<a href="http://www.reddit.com/user/evilnight/m/thefirehose%5C" rel="nofollow">http://www.reddit.com/user/evilnight/m/thefirehose\</a>) curated by <a href="/u/evilnight" rel="nofollow">/u/evilnight</a>. All subreddits are active!</p>
<p><a href="/r/music" rel="nofollow">/r/music</a><br>
<a href="/r/listentothis" rel="nofollow">/r/listentothis</a><br>
<a href="/r/WeAreTheMusicMakers" rel="nofollow">/r/WeAreTheMusicMakers</a><br>
<a href="/r/mashups" rel="nofollow">/r/mashups</a><br>
<a href="/r/vinyl" rel="nofollow">/r/vinyl</a><br>
<a href="/r/futurebeats" rel="nofollow">/r/futurebeats</a><br>
<a href="/r/musictheory" rel="nofollow">/r/musictheory</a><br>
<a href="/r/guitarlessons" rel="nofollow">/r/guitarlessons</a><br>
<a href="/r/spotify" rel="nofollow">/r/spotify</a><br>
<a href="/r/fakealbumcovers" rel="nofollow">/r/fakealbumcovers</a><br>
<a href="/r/ableton" rel="nofollow">/r/ableton</a> </p>
<h3 id="wiki_artists"><em>Artists</em></h3>
<p><a href="/r/kanye" rel="nofollow">/r/kanye</a><br>
<a href="/r/radiohead" rel="nofollow">/r/radiohead</a><br>
<a href="/r/KendrickLamar" rel="nofollow">/r/KendrickLamar</a><br>
<a href="/r/gorillaz" rel="nofollow">/r/gorillaz</a><br>
<a href="/r/frankocean" rel="nofollow">/r/frankocean</a><br>
<a href="/r/donaldglover" rel="nofollow">/r/donaldglover</a><br>
<a href="/r/eminem" rel="nofollow">/r/eminem</a><br>
<a href="/r/brockhampton" rel="nofollow">/r/brockhampton</a><br>
<a href="/r/beatles" rel="nofollow">/r/beatles</a><br>
<a href="/r/deathgrips" rel="nofollow">/r/deathgrips</a><br>
<a href="/r/pinkfloyd" rel="nofollow">/r/pinkfloyd</a> </p>
<h3 id="wiki_genres2"><em>Genres</em></h3>
<p><a href="/r/classicalmusic" rel="nofollow">/r/classicalmusic</a><br>
<a href="/r/jazz" rel="nofollow">/r/jazz</a><br>
<a href="/r/trap" rel="nofollow">/r/trap</a><br>
<a href="/r/indieheads" rel="nofollow">/r/indieheads</a><br>
<a href="/r/gamemusic" rel="nofollow">/r/gamemusic</a><br>
<a href="/r/outrun" rel="nofollow">/r/outrun</a><br>
<a href="/r/vaporwave" rel="nofollow">/r/vaporwave</a> </p>
<h4 id="wiki_electronic"><em>Electronic</em></h4>
<p><a href="/r/dubstep" rel="nofollow">/r/dubstep</a><br>
<a href="/r/electronicmusic" rel="nofollow">/r/electronicmusic</a><br>
<a href="/r/edmproduction" rel="nofollow">/r/edmproduction</a><br>
<a href="/r/EDM" rel="nofollow">/r/EDM</a> </p>
<h4 id="wiki_hip_hop"><em>Hip Hop</em></h4>
<p><a href="/r/hiphopheads" rel="nofollow">/r/hiphopheads</a><br>
<a href="/r/hiphopimages" rel="nofollow">/r/hiphopimages</a> </p>
<h4 id="wiki_metal"><em>Metal</em></h4>
<p><a href="/r/Metal" rel="nofollow">/r/Metal</a><br>
<a href="/r/Metalcore" rel="nofollow">/r/Metalcore</a> </p>
<h4 id="wiki_pop"><em>Pop</em></h4>
<p><a href="/r/spop" rel="nofollow">/r/spop</a><br>
<a href="/r/kpop" rel="nofollow">/r/kpop</a><br>
<a href="/r/funkopop" rel="nofollow">/r/funkopop</a><br>
<a href="/r/popheads" rel="nofollow">/r/popheads</a> </p>
<h3 id="wiki_instruments"><em>Instruments</em></h3>
<p><a href="/r/guitar" rel="nofollow">/r/guitar</a><br>
<a href="/r/piano" rel="nofollow">/r/piano</a><br>
<a href="/r/bass" rel="nofollow">/r/bass</a><br>
<a href="/r/drums" rel="nofollow">/r/drums</a> </p>
<h2 id="wiki_sports"><strong>Sports</strong></h2>
<p><a href="http://www.reddit.com/r/ListOfSubreddits/wiki/sports" rel="nofollow">Sports subreddits!</a><br>
<a href="http://www.reddit.com/r/ListOfSubreddits/wiki/teams" rel="nofollow">Sports team subreddits!</a> </p>
<p><a href="/r/sports" rel="nofollow">/r/sports</a><br>
<a href="/r/running" rel="nofollow">/r/running</a><br>
<a href="/r/bicycling" rel="nofollow">/r/bicycling</a><br>
<a href="/r/golf" rel="nofollow">/r/golf</a><br>
<a href="/r/fishing" rel="nofollow">/r/fishing</a><br>
<a href="/r/skiing" rel="nofollow">/r/skiing</a><br>
<a href="/r/sportsarefun" rel="nofollow">/r/sportsarefun</a><br>
<a href="/r/tennis" rel="nofollow">/r/tennis</a><br>
<a href="/r/rugbyunion" rel="nofollow">/r/rugbyunion</a><br>
<a href="/r/discgolf" rel="nofollow">/r/discgolf</a><br>
<a href="/r/cricket" rel="nofollow">/r/cricket</a><br>
<a href="/r/sailing" rel="nofollow">/r/sailing</a> </p>
<h3 id="wiki_american_football"><em>American Football</em></h3>
<p><a href="/r/nfl" rel="nofollow">/r/nfl</a><br>
<a href="/r/CFB" rel="nofollow">/r/CFB</a><br>
<a href="/r/fantasyfootball" rel="nofollow">/r/fantasyfootball</a><br>
<a href="/r/nflstreams" rel="nofollow">/r/nflstreams</a> </p>
<h4 id="wiki_american_football_teams"><em>American Football Teams</em></h4>
<p><a href="/r/patriots" rel="nofollow">/r/patriots</a><br>
<a href="/r/eagles" rel="nofollow">/r/eagles</a><br>
<a href="/r/greenbaypackers" rel="nofollow">/r/greenbaypackers</a><br>
<a href="/r/minnesotavikings" rel="nofollow">/r/minnesotavikings</a> </p>
<h3 id="wiki_baseball"><em>Baseball</em></h3>
<p><a href="/r/baseball" rel="nofollow">/r/baseball</a><br>
<a href="/r/mlb" rel="nofollow">/r/mlb</a><br>
<a href="/r/fantasybaseball" rel="nofollow">/r/fantasybaseball</a> </p>
<h3 id="wiki_basketball"><em>Basketball</em></h3>
<p><a href="/r/nba" rel="nofollow">/r/nba</a><br>
<a href="/r/collegebasketball" rel="nofollow">/r/collegebasketball</a><br>
<a href="/r/nbastreams" rel="nofollow">/r/nbastreams</a> </p>
<h4 id="wiki_teams"><em>Teams</em></h4>
<p><a href="/r/warriors" rel="nofollow">/r/warriors</a><br>
<a href="/r/lakers" rel="nofollow">/r/lakers</a><br>
<a href="/r/bostonceltics" rel="nofollow">/r/bostonceltics</a><br>
<a href="/r/torontoraptors" rel="nofollow">/r/torontoraptors</a> </p>
<h3 id="wiki_boards"><em>Boards</em></h3>
<p><a href="/r/skateboarding" rel="nofollow">/r/skateboarding</a><br>
<a href="/r/snowboarding" rel="nofollow">/r/snowboarding</a><br>
<a href="/r/longboarding" rel="nofollow">/r/longboarding</a> </p>
<h3 id="wiki_cars"><em>Cars</em></h3>
<p><a href="/r/formula1" rel="nofollow">/r/formula1</a><br>
<a href="/r/Nascar" rel="nofollow">/r/Nascar</a> </p>
<h3 id="wiki_fighting"><em>Fighting</em></h3>
<p><a href="/r/MMA" rel="nofollow">/r/MMA</a><br>
<a href="/r/squaredcircle" rel="nofollow">/r/squaredcircle</a><br>
<a href="/r/theocho" rel="nofollow">/r/theocho</a><br>
<a href="/r/ufc" rel="nofollow">/r/ufc</a><br>
<a href="/r/boxing" rel="nofollow">/r/boxing</a><br>
<a href="/r/wwe" rel="nofollow">/r/wwe</a><br>
<a href="/r/MMAStreams" rel="nofollow">/r/MMAStreams</a> </p>
<h3 id="wiki_hockey"><em>Hockey</em></h3>
<p><a href="/r/hockey" rel="nofollow">/r/hockey</a><br>
<a href="/r/nhl" rel="nofollow">/r/nhl</a><br>
<a href="/r/nhlstreams" rel="nofollow">/r/nhlstreams</a><br>
<a href="/r/leafs" rel="nofollow">/r/leafs</a> </p>
<h3 id="wiki_olympics"><em>Olympics</em></h3>
<p><a href="/r/olympics" rel="nofollow">/r/olympics</a><br>
<a href="/r/apocalympics2016" rel="nofollow">/r/apocalympics2016</a> </p>
<h3 id="wiki_soccer"><em>Soccer</em></h3>
<p><a href="/r/soccer" rel="nofollow">/r/soccer</a><br>
<a href="/r/worldcup" rel="nofollow">/r/worldcup</a><br>
<a href="/r/Bundesliga" rel="nofollow">/r/Bundesliga</a><br>
<a href="/r/futbol" rel="nofollow">/r/futbol</a><br>
<a href="/r/soccerstreams" rel="nofollow">/r/soccerstreams</a><br>
<a href="/r/MLS" rel="nofollow">/r/MLS</a><br>
<a href="/r/fantasypl" rel="nofollow">/r/fantasypl</a> </p>
<h4 id="wiki_soccer_teams"><em>Soccer Teams</em></h4>
<p><a href="/r/gunners" rel="nofollow">/r/gunners</a><br>
<a href="/r/reddevils" rel="nofollow">/r/reddevils</a><br>
<a href="/r/LiverpoolFC" rel="nofollow">/r/LiverpoolFC</a><br>
<a href="/r/chelseafc" rel="nofollow">/r/chelseafc</a> </p>
<h2 id="wiki_tv"><strong>TV</strong></h2>
<p><a href="/r/Television" rel="nofollow">/r/Television</a><br>
<a href="/r/marvelstudios" rel="nofollow">/r/marvelstudios</a><br>
<a href="/r/japanesegameshows" rel="nofollow">/r/japanesegameshows</a><br>
<a href="/r/shield" rel="nofollow">/r/shield</a><br>
<a href="/r/cordcutters" rel="nofollow">/r/cordcutters</a><br>
<a href="/r/offlinetv" rel="nofollow">/r/offlinetv</a><br>
<a href="/r/tvdetails" rel="nofollow">/r/tvdetails</a> </p>
<h3 id="wiki_individual_shows"><em>Individual Shows</em></h3>
<p><a href="/r/GameOfThrones" rel="nofollow">/r/GameOfThrones</a><br>
<a href="/r/BreakingBad" rel="nofollow">/r/BreakingBad</a><br>
<a href="/r/thewalkingdead" rel="nofollow">/r/thewalkingdead</a><br>
<a href="/r/community" rel="nofollow">/r/community</a><br>
<a href="/r/arresteddevelopment" rel="nofollow">/r/arresteddevelopment</a><br>
<a href="/r/topgear" rel="nofollow">/r/topgear</a><br>
<a href="/r/StarTrek" rel="nofollow">/r/StarTrek</a> <a href="https://www.reddit.com/r/Treknobabble/wiki/other" rel="nofollow">More here!</a><br>
<a href="/r/HIMYM" rel="nofollow">/r/HIMYM</a><br>
<a href="/r/firefly" rel="nofollow">/r/firefly</a><br>
<a href="/r/PandR" rel="nofollow">/r/PandR</a><br>
<a href="/r/Sherlock" rel="nofollow">/r/Sherlock</a><br>
<a href="/r/DunderMifflin" rel="nofollow">/r/DunderMifflin</a> (The Office)<br>
<a href="/r/BetterCallSaul" rel="nofollow">/r/BetterCallSaul</a><br>
<a href="/r/TrueDetective" rel="nofollow">/r/TrueDetective</a><br>
<a href="/r/houseofcards" rel="nofollow">/r/houseofcards</a><br>
<a href="/r/MakingaMurderer" rel="nofollow">/r/MakingaMurderer</a><br>
<a href="/r/FlashTV" rel="nofollow">/r/FlashTV</a><br>
<a href="/r/trailerparkboys" rel="nofollow">/r/trailerparkboys</a><br>
<a href="/r/mrrobot" rel="nofollow">/r/mrrobot</a><br>
<a href="/r/siliconvalleyhbo" rel="nofollow">/r/siliconvalleyhbo</a><br>
<a href="/r/strangerthings" rel="nofollow">/r/strangerthings</a><br>
<a href="/r/supernatural" rel="nofollow">/r/supernatural</a><br>
<a href="/r/thegrandtour" rel="nofollow">/r/thegrandtour</a><br>
<a href="/r/AmericanHorrorStory" rel="nofollow">/r/AmericanHorrorStory</a><br>
<a href="/r/rupaulsdragrace" rel="nofollow">/r/rupaulsdragrace</a><br>
<a href="/r/westworld" rel="nofollow">/r/westworld</a><br>
<a href="/r/blackmirror" rel="nofollow">/r/blackmirror</a><br>
<a href="/r/FilthyFrank" rel="nofollow">/r/FilthyFrank</a><br>
<a href="/r/orangeisthenewblack" rel="nofollow">/r/orangeisthenewblack</a><br>
<a href="/r/twinpeaks" rel="nofollow">/r/twinpeaks</a><br>
<a href="/r/bigbrother" rel="nofollow">/r/bigbrother</a><br>
<a href="/r/brooklynninenine" rel="nofollow">/r/brooklynninenine</a><br>
<a href="/r/scrubs" rel="nofollow">/r/scrubs</a><br>
<a href="/r/howyoudoin" rel="nofollow">/r/howyoudoin</a> (Friends)<br>
<a href="/r/30rock" rel="nofollow">/r/30rock</a><br>
<a href="/r/lifeisstrange" rel="nofollow">/r/lifeisstrange</a><br>
<a href="/r/survivor" rel="nofollow">/r/survivor</a><br>
<a href="/r/riverdale" rel="nofollow">/r/riverdale</a> </p>
<h4 id="wiki_animated"><em>Animated</em></h4>
<p><a href="/r/Pokemon" rel="nofollow">/r/Pokemon</a><br>
<a href="/r/AdventureTime" rel="nofollow">/r/AdventureTime</a><br>
<a href="/r/futurama" rel="nofollow">/r/futurama</a><br>
<a href="/r/TheLastAirbender" rel="nofollow">/r/TheLastAirbender</a><br>
<a href="/r/ArcherFX" rel="nofollow">/r/ArcherFX</a><br>
<a href="/r/southpark" rel="nofollow">/r/southpark</a><br>
<a href="/r/TheSimpsons" rel="nofollow">/r/TheSimpsons</a><br>
<a href="/r/mylittlepony" rel="nofollow">/r/mylittlepony</a><br>
<a href="/r/rickandmorty" rel="nofollow">/r/rickandmorty</a><br>
<a href="/r/naruto" rel="nofollow">/r/naruto</a><br>
<a href="/r/stevenuniverse" rel="nofollow">/r/stevenuniverse</a><br>
<a href="/r/onepunchman" rel="nofollow">/r/onepunchman</a><br>
<a href="/r/BobsBurgers" rel="nofollow">/r/BobsBurgers</a><br>
<a href="/r/BoJackHorseman" rel="nofollow">/r/BoJackHorseman</a><br>
<a href="/r/gravityfalls" rel="nofollow">/r/gravityfalls</a><br>
<a href="/r/familyguy" rel="nofollow">/r/familyguy</a><br>
<a href="/r/kingofthehill" rel="nofollow">/r/kingofthehill</a><br>
<a href="/r/spongebob" rel="nofollow">/r/spongebob</a> </p>
<h5 id="wiki_dragon_ball_z"><em>Dragon Ball Z</em></h5>
<p><a href="/r/dbz" rel="nofollow">/r/dbz</a><br>
<a href="/r/DBZDokkanBattle" rel="nofollow">/r/DBZDokkanBattle</a><br>
<a href="/r/dragonballfighterz" rel="nofollow">/r/dragonballfighterz</a> </p>
<h4 id="wiki_doctor_who"><em>Doctor Who</em></h4>
<p><a href="/r/doctorwho" rel="nofollow">/r/doctorwho</a><br>
<a href="/r/gallifrey" rel="nofollow">/r/gallifrey</a> </p>
<h4 id="wiki_it.27s_always_sunny_in_philadelphia"><em>It's Always Sunny in Philadelphia</em></h4>
<p><a href="/r/IASIP" rel="nofollow">/r/IASIP</a><br>
<a href="/r/the_dennis" rel="nofollow">/r/the_dennis</a> </p>
<h4 id="wiki_seinfeld"><em>Seinfeld</em></h4>
<p><a href="/r/seinfeld" rel="nofollow">/r/seinfeld</a><br>
<a href="/r/redditwritesseinfeld" rel="nofollow">/r/redditwritesseinfeld</a><br>
<a href="/r/seinfeldgifs" rel="nofollow">/r/seinfeldgifs</a> </p>
<h3 id="wiki_netflix_related"><em>Netflix Related</em></h3>
<p><a href="/r/NetflixBestOf" rel="nofollow">/r/NetflixBestOf</a><br>
<a href="/r/Netflix" rel="nofollow">/r/Netflix</a><br>
<a href="/r/bestofnetflix" rel="nofollow">/r/bestofnetflix</a> </p>
<hr>
<h1 id="wiki_hobbies.2Foccupations"><strong>Hobbies/Occupations</strong></h1>
<h2 id="wiki_general4"><strong>General</strong></h2>
<p><a href="/r/DIY" rel="nofollow">/r/DIY</a>   (<a href="http://www.reddit.com/r/ListOfSubreddits/wiki/diy" rel="nofollow">List of DIY subreddits!</a>)<br>
<a href="/r/cosplay" rel="nofollow">/r/cosplay</a><br>
<a href="/r/woodworking" rel="nofollow">/r/woodworking</a><br>
<a href="/r/somethingimade" rel="nofollow">/r/somethingimade</a><br>
<a href="/r/architecture" rel="nofollow">/r/architecture</a><br>
<a href="/r/CoolGuides" rel="nofollow">/r/CoolGuides</a><br>
<a href="/r/WorldBuilding" rel="nofollow">/r/WorldBuilding</a><br>
<a href="/r/ifyoulikeblank" rel="nofollow">/r/ifyoulikeblank</a><br>
<a href="/r/DiWHY" rel="nofollow">/r/DiWHY</a><br>
<a href="/r/knitting" rel="nofollow">/r/knitting</a><br>
<a href="/r/sewing" rel="nofollow">/r/sewing</a><br>
<a href="/r/modelmakers" rel="nofollow">/r/modelmakers</a><br>
<a href="/r/crochet" rel="nofollow">/r/crochet</a><br>
<a href="/r/ProtectAndServe" rel="nofollow">/r/ProtectAndServe</a><br>
<a href="/r/RTLSDR" rel="nofollow">/r/RTLSDR</a><br>
<a href="/r/digitalnomad" rel="nofollow">/r/digitalnomad</a><br>
<a href="/r/FastWorkers" rel="nofollow">/r/FastWorkers</a><br>
<a href="/r/accounting" rel="nofollow">/r/accounting</a><br>
<a href="/r/preppers" rel="nofollow">/r/preppers</a><br>
<a href="/r/redneckengineering" rel="nofollow">/r/redneckengineering</a><br>
<a href="/r/crossstitch" rel="nofollow">/r/crossstitch</a><br>
<a href="/r/dumpsterdiving" rel="nofollow">/r/dumpsterdiving</a><br>
<a href="/r/gunpla" rel="nofollow">/r/gunpla</a><br>
<a href="/r/urbanplanning" rel="nofollow">/r/urbanplanning</a><br>
<a href="/r/cubers" rel="nofollow">/r/cubers</a><br>
<a href="/r/blacksmith" rel="nofollow">/r/blacksmith</a> </p>
<h2 id="wiki_aquariums"><strong>Aquariums</strong></h2>
<p><a href="/r/aquariums" rel="nofollow">/r/aquariums</a><br>
<a href="/r/plantedtank" rel="nofollow">/r/plantedtank</a> </p>
<h2 id="wiki_arts.2Fwriting"><strong>Arts/Writing</strong></h2>
<p><a href="/r/art" rel="nofollow">/r/art</a><br>
<a href="/r/Drawing" rel="nofollow">/r/Drawing</a><br>
<a href="/r/crafts" rel="nofollow">/r/crafts</a><br>
<a href="/r/alternativeart" rel="nofollow">/r/alternativeart</a><br>
<a href="/r/sketchdaily" rel="nofollow">/r/sketchdaily</a><br>
<a href="/r/artporn" rel="nofollow">/r/artporn</a><br>
<a href="/r/glitch_art" rel="nofollow">/r/glitch_art</a><br>
<a href="/r/coloringcorruptions" rel="nofollow">/r/coloringcorruptions</a><br>
<a href="/r/restofthefuckingowl" rel="nofollow">/r/restofthefuckingowl</a><br>
<a href="/r/DisneyVacation" rel="nofollow">/r/DisneyVacation</a><br>
<a href="/r/illustration" rel="nofollow">/r/illustration</a> </p>
<h3 id="wiki_writing"><em>Writing</em></h3>
<p><a href="/r/Writing" rel="nofollow">/r/Writing</a><br>
<a href="/r/writingprompts" rel="nofollow">/r/writingprompts</a><br>
<a href="/r/screenwriting" rel="nofollow">/r/screenwriting</a><br>
<a href="/r/fountainpens" rel="nofollow">/r/fountainpens</a><br>
<a href="/r/calligraphy" rel="nofollow">/r/calligraphy</a><br>
<a href="/r/handwriting" rel="nofollow">/r/handwriting</a><br>
<a href="/r/twosentencehorror" rel="nofollow">/r/twosentencehorror</a> </p>
<h2 id="wiki_automotive"><strong>Automotive</strong></h2>
<p><a href="/r/cars" rel="nofollow">/r/cars</a><br>
<a href="/r/motorcycles" rel="nofollow">/r/motorcycles</a>  (<a href="http://www.reddit.com/user/noeatnosleep/m/motorcycles" rel="nofollow">motorcycle multi</a> compiled by <a href="/u/noeatnosleep" rel="nofollow">/u/noeatnosleep</a>. Not all active.)<br>
<a href="/r/carporn" rel="nofollow">/r/carporn</a><br>
<a href="/r/justrolledintotheshop" rel="nofollow">/r/justrolledintotheshop</a><br>
<a href="/r/Shitty_Car_Mods" rel="nofollow">/r/Shitty_Car_Mods</a><br>
<a href="/r/autos" rel="nofollow">/r/autos</a><br>
<a href="/r/roadcam" rel="nofollow">/r/roadcam</a><br>
<a href="/r/AutoDetailing" rel="nofollow">/r/AutoDetailing</a><br>
<a href="/r/awesomecarmods" rel="nofollow">/r/awesomecarmods</a><br>
<a href="/r/projectcar" rel="nofollow">/r/projectcar</a><br>
<a href="/r/cartalk" rel="nofollow">/r/cartalk</a><br>
<a href="/r/tiresaretheenemy" rel="nofollow">/r/tiresaretheenemy</a> </p>
<h3 id="wiki_car_companies"><em>Car companies</em></h3>
<p><a href="/r/subaru" rel="nofollow">/r/subaru</a><br>
<a href="/r/teslamotors" rel="nofollow">/r/teslamotors</a><br>
<a href="/r/bmw" rel="nofollow">/r/bmw</a><br>
<a href="/r/jeep" rel="nofollow">/r/jeep</a> </p>
<h2 id="wiki_design"><strong>Design</strong></h2>
<p><a href="/r/CrappyDesign" rel="nofollow">/r/CrappyDesign</a><br>
<a href="/r/web_design" rel="nofollow">/r/web_design</a><br>
<a href="/r/graphic_design" rel="nofollow">/r/graphic_design</a><br>
<a href="/r/design" rel="nofollow">/r/design</a><br>
<a href="/r/designporn" rel="nofollow">/r/designporn</a><br>
<a href="/r/InteriorDesign" rel="nofollow">/r/InteriorDesign</a><br>
<a href="/r/ATBGE" rel="nofollow">/r/ATBGE</a><br>
<a href="/r/dontdeadopeninside" rel="nofollow">/r/dontdeadopeninside</a><br>
<a href="/r/assholedesign" rel="nofollow">/r/assholedesign</a><br>
<a href="/r/keming" rel="nofollow">/r/keming</a><br>
<a href="/r/logodesign" rel="nofollow">/r/logodesign</a><br>
<a href="/r/tombstoning" rel="nofollow">/r/tombstoning</a> </p>
<h2 id="wiki_fake_it_til_you_make_it"><strong>Fake it til you make it</strong></h2>
<p><a href="/r/actlikeyoubelong" rel="nofollow">/r/actlikeyoubelong</a><br>
<a href="/r/irlsmurfing" rel="nofollow">/r/irlsmurfing</a> </p>
<h2 id="wiki_guns.2Fcombat"><strong>Guns/Combat</strong></h2>
<h3 id="wiki_combat"><strong>Combat</strong></h3>
<p><a href="/r/MilitaryPorn" rel="nofollow">/r/MilitaryPorn</a><br>
<a href="/r/military" rel="nofollow">/r/military</a><br>
<a href="/r/combatfootage" rel="nofollow">/r/combatfootage</a><br>
<a href="/r/militarygfys" rel="nofollow">/r/militarygfys</a><br>
<a href="/r/army" rel="nofollow">/r/army</a><br>
<a href="/r/warshipporn" rel="nofollow">/r/warshipporn</a> </p>
<h3 id="wiki_guns"><strong>Guns</strong></h3>
<p><a href="/r/guns" rel="nofollow">/r/guns</a><br>
<a href="/r/gunporn" rel="nofollow">/r/gunporn</a><br>
<a href="/r/gundeals" rel="nofollow">/r/gundeals</a><br>
<a href="/r/ar15" rel="nofollow">/r/ar15</a><br>
<a href="/r/firearms" rel="nofollow">/r/firearms</a><br>
<a href="/r/ccw" rel="nofollow">/r/ccw</a><br>
<a href="/r/airsoft" rel="nofollow">/r/airsoft</a> </p>
<h2 id="wiki_job_finding"><strong>Job finding</strong></h2>
<p><a href="/r/Jobs" rel="nofollow">/r/Jobs</a><br>
<a href="/r/forhire" rel="nofollow">/r/forhire</a><br>
<a href="/r/cscareerquestions" rel="nofollow">/r/cscareerquestions</a><br>
<a href="/r/workonline" rel="nofollow">/r/workonline</a> </p>
<h2 id="wiki_music2"><strong>Music</strong></h2>
<p><a href="/r/guitar" rel="nofollow">/r/guitar</a><br>
<a href="/r/WeAreTheMusicMakers" rel="nofollow">/r/WeAreTheMusicMakers</a><br>
<a href="/r/edmproduction" rel="nofollow">/r/edmproduction</a><br>
<a href="/r/piano" rel="nofollow">/r/piano</a><br>
<a href="/r/ableton" rel="nofollow">/r/ableton</a><br>
<a href="/r/drums" rel="nofollow">/r/drums</a><br>
<a href="/r/FL_Studio" rel="nofollow">/r/FL_Studio</a> </p>
<h2 id="wiki_outdoors"><strong>Outdoors</strong></h2>
<p><a href="/r/gardening" rel="nofollow">/r/gardening</a><br>
<a href="/r/urbanexploration" rel="nofollow">/r/urbanexploration</a><br>
<a href="/r/survival" rel="nofollow">/r/survival</a><br>
<a href="/r/backpacking" rel="nofollow">/r/backpacking</a><br>
<a href="/r/camping" rel="nofollow">/r/camping</a><br>
<a href="/r/homestead" rel="nofollow">/r/homestead</a><br>
<a href="/r/MTB" rel="nofollow">/r/MTB</a><br>
<a href="/r/outdoors" rel="nofollow">/r/outdoors</a><br>
<a href="/r/wildernessbackpacking" rel="nofollow">/r/wildernessbackpacking</a><br>
<a href="/r/campinggear" rel="nofollow">/r/campinggear</a> </p>
<h3 id="wiki_hiking"><strong>Hiking</strong></h3>
<p><a href="/r/campingandhiking" rel="nofollow">/r/campingandhiking</a><br>
<a href="/r/hiking" rel="nofollow">/r/hiking</a><br>
<a href="/r/ultralight" rel="nofollow">/r/ultralight</a> </p>
<h2 id="wiki_photography.2Ffilm"><strong>Photography/Film</strong></h2>
<p><a href="/r/photography" rel="nofollow">/r/photography</a><br>
<a href="/r/itookapicture" rel="nofollow">/r/itookapicture</a><br>
<a href="/r/Filmmakers" rel="nofollow">/r/Filmmakers</a><br>
<a href="/r/astrophotography" rel="nofollow">/r/astrophotography</a><br>
<a href="/r/analog" rel="nofollow">/r/analog</a><br>
<a href="/r/photocritique" rel="nofollow">/r/photocritique</a> </p>
<h2 id="wiki_planes"><strong>Planes</strong></h2>
<p><a href="/r/aviation" rel="nofollow">/r/aviation</a><br>
<a href="/r/flying" rel="nofollow">/r/flying</a> </p>
<h2 id="wiki_tech_related"><strong>Tech Related</strong></h2>
<p><a href="/r/sysadmin" rel="nofollow">/r/sysadmin</a><br>
<a href="/r/engineering" rel="nofollow">/r/engineering</a><br>
<a href="/r/compsci" rel="nofollow">/r/compsci</a><br>
<a href="/r/webdev" rel="nofollow">/r/webdev</a><br>
<a href="/r/programmerhumor" rel="nofollow">/r/programmerhumor</a><br>
<a href="/r/graphic_design" rel="nofollow">/r/graphic_design</a><br>
<a href="/r/mechanicalkeyboards" rel="nofollow">/r/mechanicalkeyboards</a><br>
<a href="/r/reverseengineering" rel="nofollow">/r/reverseengineering</a><br>
<a href="/r/itsaunixsystem" rel="nofollow">/r/itsaunixsystem</a><br>
<a href="/r/plex" rel="nofollow">/r/plex</a><br>
<a href="/r/multicopter" rel="nofollow">/r/multicopter</a><br>
<a href="/r/programminghorror" rel="nofollow">/r/programminghorror</a> </p>
<h3 id="wiki_coding2"><em>Coding</em></h3>
<p><a href="/r/dailyprogrammer" rel="nofollow">/r/dailyprogrammer</a><br>
<a href="/r/coding" rel="nofollow">/r/coding</a><br>
<a href="/r/python" rel="nofollow">/r/python</a><br>
<a href="/r/java" rel="nofollow">/r/java</a><br>
<a href="/r/cpp" rel="nofollow">/r/cpp</a> </p>
<h3 id="wiki_pc_building"><em>PC Building</em></h3>
<p><a href="/r/buildapc" rel="nofollow">/r/buildapc</a><br>
<a href="/r/buildapcsales" rel="nofollow">/r/buildapcsales</a><br>
<a href="/r/buildapcforme" rel="nofollow">/r/buildapcforme</a> </p>
<h3 id="wiki_tech_support"><em>Tech Support</em></h3>
<p><a href="/r/talesfromtechsupport" rel="nofollow">/r/talesfromtechsupport</a><br>
<a href="/r/techsupportgore" rel="nofollow">/r/techsupportgore</a><br>
<a href="/r/techsupport" rel="nofollow">/r/techsupport</a><br>
<a href="/r/softwaregore" rel="nofollow">/r/softwaregore</a><br>
<a href="/r/iiiiiiitttttttttttt" rel="nofollow">/r/iiiiiiitttttttttttt</a> </p>
<h2 id="wiki_tools"><strong>Tools</strong></h2>
<p><a href="/r/watches" rel="nofollow">/r/watches</a><br>
<a href="/r/lockpicking" rel="nofollow">/r/lockpicking</a><br>
<a href="/r/knives" rel="nofollow">/r/knives</a><br>
<a href="/r/specializedtools" rel="nofollow">/r/specializedtools</a><br>
<a href="/r/knifeclub" rel="nofollow">/r/knifeclub</a> </p>
<h2 id="wiki_travel"><strong>Travel</strong></h2>
<p><a href="/r/travel" rel="nofollow">/r/travel</a><br>
<a href="/r/solotravel" rel="nofollow">/r/solotravel</a><br>
<a href="/r/japantravel" rel="nofollow">/r/japantravel</a> </p>
<hr>
<h1 id="wiki_lifestyle"><strong>Lifestyle</strong></h1>
<h2 id="wiki_general5"><strong>General</strong></h2>
<p><a href="/r/LifeProTips" rel="nofollow">/r/LifeProTips</a><br>
<a href="/r/lifehacks" rel="nofollow">/r/lifehacks</a><br>
<a href="/r/geek" rel="nofollow">/r/geek</a><br>
<a href="/r/EDC" rel="nofollow">/r/EDC</a><br>
<a href="/r/simpleliving" rel="nofollow">/r/simpleliving</a><br>
<a href="/r/tinyhouses" rel="nofollow">/r/tinyhouses</a><br>
<a href="/r/rainmeter" rel="nofollow">/r/rainmeter</a><br>
<a href="/r/vandwellers" rel="nofollow">/r/vandwellers</a><br>
<a href="/r/UnethicalLifeProTips" rel="nofollow">/r/UnethicalLifeProTips</a> </p>
<h3 id="wiki_gender"><em>Gender</em></h3>
<p><a href="/r/malelifestyle" rel="nofollow">/r/malelifestyle</a><br>
<a href="/r/malelivingspace" rel="nofollow">/r/malelivingspace</a><br>
<a href="/r/TheGirlSurvivalGuide" rel="nofollow">/r/TheGirlSurvivalGuide</a> </p>
<h3 id="wiki_home"><em>Home</em></h3>
<p><a href="/r/homeimprovement" rel="nofollow">/r/homeimprovement</a><br>
<a href="/r/homelab" rel="nofollow">/r/homelab</a><br>
<a href="/r/homeautomation" rel="nofollow">/r/homeautomation</a><br>
<a href="/r/battlestations" rel="nofollow">/r/battlestations</a><br>
<a href="/r/hometheater" rel="nofollow">/r/hometheater</a> </p>
<h2 id="wiki_communities"><strong>Communities</strong></h2>
<p><a href="/r/teenagers" rel="nofollow">/r/teenagers</a><br>
<a href="/r/introvert" rel="nofollow">/r/introvert</a><br>
<a href="/r/ADHD" rel="nofollow">/r/ADHD</a><br>
<a href="/r/totallynotrobots" rel="nofollow">/r/totallynotrobots</a><br>
<a href="/r/polyamory" rel="nofollow">/r/polyamory</a><br>
<a href="/r/teachers" rel="nofollow">/r/teachers</a><br>
<a href="/r/aliensamongus" rel="nofollow">/r/aliensamongus</a><br>
<a href="/r/neverbrokeabone" rel="nofollow">/r/neverbrokeabone</a><br>
<a href="/r/bipolar" rel="nofollow">/r/bipolar</a> </p>
<h3 id="wiki_body.2Fdiet"><em>Body/Diet</em></h3>
<p><a href="/r/beards" rel="nofollow">/r/beards</a><br>
<a href="/r/vegan" rel="nofollow">/r/vegan</a><br>
<a href="/r/swoleacceptance" rel="nofollow">/r/swoleacceptance</a><br>
<a href="/r/tall" rel="nofollow">/r/tall</a> </p>
<h3 id="wiki_lgbt"><em>LGBT</em></h3>
<p><a href="/r/lgbt" rel="nofollow">/r/lgbt</a><br>
<a href="/r/gaybros" rel="nofollow">/r/gaybros</a><br>
<a href="/r/actuallesbians" rel="nofollow">/r/actuallesbians</a><br>
<a href="/r/gaymers" rel="nofollow">/r/gaymers</a><br>
<a href="/r/bisexual" rel="nofollow">/r/bisexual</a><br>
<a href="/r/askgaybros" rel="nofollow">/r/askgaybros</a><br>
<a href="/r/ainbow" rel="nofollow">/r/ainbow</a><br>
<a href="/r/gay" rel="nofollow">/r/gay</a><br>
<a href="/r/gay_irl" rel="nofollow">/r/gay_irl</a> </p>
<h4 id="wiki_transgender"><em>Transgender</em></h4>
<p><a href="/r/asktransgender" rel="nofollow">/r/asktransgender</a><br>
<a href="/r/transgender" rel="nofollow">/r/transgender</a> </p>
<h3 id="wiki_parenting"><em>Parenting</em></h3>
<p><a href="/r/parenting" rel="nofollow">/r/parenting</a><br>
<a href="/r/daddit" rel="nofollow">/r/daddit</a><br>
<a href="/r/babybumps" rel="nofollow">/r/babybumps</a> </p>
<h2 id="wiki_drugs"><strong>Drugs</strong></h2>
<h3 id="wiki_alcohol"><em>Alcohol</em></h3>
<p><a href="/r/drunk" rel="nofollow">/r/drunk</a><br>
<a href="/r/scotch" rel="nofollow">/r/scotch</a><br>
<a href="/r/stopdrinking" rel="nofollow">/r/stopdrinking</a><br>
<a href="/r/cocktails" rel="nofollow">/r/cocktails</a><br>
<a href="/r/wine" rel="nofollow">/r/wine</a><br>
<a href="/r/bourbon" rel="nofollow">/r/bourbon</a><br>
<a href="/r/whiskey" rel="nofollow">/r/whiskey</a> </p>
<h4 id="wiki_beer"><em>Beer</em></h4>
<p><a href="/r/beer" rel="nofollow">/r/beer</a><br>
<a href="/r/homebrewing" rel="nofollow">/r/homebrewing</a><br>
<a href="/r/showerbeer" rel="nofollow">/r/showerbeer</a><br>
<a href="/r/beerporn" rel="nofollow">/r/beerporn</a> </p>
<h3 id="wiki_marijuana"><em>Marijuana</em></h3>
<p><a href="/r/trees" rel="nofollow">/r/trees</a><br>
<a href="/r/marijuana" rel="nofollow">/r/marijuana</a><br>
<a href="/r/microgrowery" rel="nofollow">/r/microgrowery</a><br>
<a href="/r/eldertrees" rel="nofollow">/r/eldertrees</a><br>
<a href="/r/see" rel="nofollow">/r/see</a><br>
<a href="/r/leaves" rel="nofollow">/r/leaves</a><br>
<a href="/r/weed" rel="nofollow">/r/weed</a><br>
<a href="/r/weedstocks" rel="nofollow">/r/weedstocks</a><br>
<a href="/r/cannabis" rel="nofollow">/r/cannabis</a> </p>
<h3 id="wiki_other_drugs"><em>Other drugs</em></h3>
<p><a href="/r/drugs" rel="nofollow">/r/drugs</a><br>
<a href="/r/electronic_cigarette" rel="nofollow">/r/electronic_cigarette</a><br>
<a href="/r/stonerengineering" rel="nofollow">/r/stonerengineering</a><br>
<a href="/r/Nootropics" rel="nofollow">/r/Nootropics</a><br>
<a href="/r/LSD" rel="nofollow">/r/LSD</a><br>
<a href="/r/vaporents" rel="nofollow">/r/vaporents</a><br>
<a href="/r/Vaping" rel="nofollow">/r/Vaping</a><br>
<a href="/r/stopsmoking" rel="nofollow">/r/stopsmoking</a><br>
<a href="/r/shrooms" rel="nofollow">/r/shrooms</a><br>
<a href="/r/dmt" rel="nofollow">/r/dmt</a> </p>
<h2 id="wiki_exercise.2Fhealth"><strong>Exercise/Health</strong></h2>
<p><a href="/r/GetMotivated" rel="nofollow">/r/GetMotivated</a><br>
<a href="/r/health" rel="nofollow">/r/health</a><br>
<a href="/r/ZenHabits" rel="nofollow">/r/ZenHabits</a><br>
<a href="/r/Medicine" rel="nofollow">/r/Medicine</a> </p>
<h3 id="wiki_mental"><em>Mental</em></h3>
<p><a href="/r/LucidDreaming" rel="nofollow">/r/LucidDreaming</a><br>
<a href="/r/meditation" rel="nofollow">/r/meditation</a><br>
<a href="/r/Psychonaut" rel="nofollow">/r/Psychonaut</a><br>
<a href="/r/mentalhealth" rel="nofollow">/r/mentalhealth</a> </p>
<h3 id="wiki_physical"><em>Physical</em></h3>
<p>For more fitness subreddits, see <a href="http://www.reddit.com/r/Fitness/wiki/related_subreddits" rel="nofollow">this list</a> compiled by <a href="/r/Fitness" rel="nofollow">/r/Fitness</a>!<br>
Note: Many of those subreddits are tiny/inactive.</p>
<p><a href="/r/Fitness" rel="nofollow">/r/Fitness</a><br>
<a href="/r/xxfitness" rel="nofollow">/r/xxfitness</a> </p>
<h4 id="wiki_diet"><em>Diet</em></h4>
<p><a href="/r/fitmeals" rel="nofollow">/r/fitmeals</a><br>
<a href="/r/paleo" rel="nofollow">/r/paleo</a><br>
<a href="/r/nutrition" rel="nofollow">/r/nutrition</a><br>
<a href="/r/vegetarian" rel="nofollow">/r/vegetarian</a><br>
<a href="/r/leangains" rel="nofollow">/r/leangains</a><br>
<a href="/r/HealthyFood" rel="nofollow">/r/HealthyFood</a><br>
<a href="/r/intermittentfasting" rel="nofollow">/r/intermittentfasting</a><br>
<a href="/r/fasting" rel="nofollow">/r/fasting</a> </p>
<h5 id="wiki_keto"><em>Keto</em></h5>
<p><a href="/r/keto" rel="nofollow">/r/keto</a><br>
<a href="/r/ketorecipes" rel="nofollow">/r/ketorecipes</a><br>
<a href="/r/ketogains" rel="nofollow">/r/ketogains</a> </p>
<h4 id="wiki_exercise"><em>Exercise</em></h4>
<p><a href="/r/bicycling" rel="nofollow">/r/bicycling</a><br>
<a href="/r/yoga" rel="nofollow">/r/yoga</a><br>
<a href="/r/skateboarding" rel="nofollow">/r/skateboarding</a><br>
<a href="/r/climbing" rel="nofollow">/r/climbing</a><br>
<a href="/r/backpacking" rel="nofollow">/r/backpacking</a><br>
<a href="/r/bjj" rel="nofollow">/r/bjj</a><br>
<a href="/r/skiing" rel="nofollow">/r/skiing</a><br>
<a href="/r/crossfit" rel="nofollow">/r/crossfit</a> </p>
<h5 id="wiki_lifting.2Fweights"><em>Lifting/Weights</em></h5>
<p><a href="/r/bodybuilding" rel="nofollow">/r/bodybuilding</a><br>
<a href="/r/WeightRoom" rel="nofollow">/r/WeightRoom</a><br>
<a href="/r/powerlifting" rel="nofollow">/r/powerlifting</a> </p>
<h5 id="wiki_running"><em>Running</em></h5>
<p><a href="/r/running" rel="nofollow">/r/running</a><br>
<a href="/r/c25k" rel="nofollow">/r/c25k</a> </p>
<h4 id="wiki_weight.2Fbody_shape_control"><em>Weight/Body Shape Control</em></h4>
<p><a href="/r/loseit" rel="nofollow">/r/loseit</a><br>
<a href="/r/bodyweightfitness" rel="nofollow">/r/bodyweightfitness</a><br>
<a href="/r/gainit" rel="nofollow">/r/gainit</a><br>
<a href="/r/swoleacceptance" rel="nofollow">/r/swoleacceptance</a><br>
<a href="/r/flexibility" rel="nofollow">/r/flexibility</a> </p>
<h5 id="wiki_progress_pictures"><em>Progress Pictures</em></h5>
<p><a href="/r/progresspics" rel="nofollow">/r/progresspics</a><br>
<a href="/r/brogress" rel="nofollow">/r/brogress</a> </p>
<h2 id="wiki_fashion.2Fbeauty"><strong>Fashion/Beauty</strong></h2>
<h3 id="wiki_body_image"><em>Body Image</em></h3>
<p><a href="/r/makeupaddiction" rel="nofollow">/r/makeupaddiction</a><br>
<a href="/r/SkincareAddiction" rel="nofollow">/r/SkincareAddiction</a><br>
<a href="/r/beards" rel="nofollow">/r/beards</a><br>
<a href="/r/wicked_edge" rel="nofollow">/r/wicked_edge</a><br>
<a href="/r/RedditLaqueristas" rel="nofollow">/r/RedditLaqueristas</a><br>
<a href="/r/AsianBeauty" rel="nofollow">/r/AsianBeauty</a><br>
<a href="/r/piercing" rel="nofollow">/r/piercing</a> </p>
<h4 id="wiki_hair"><em>Hair</em></h4>
<p><a href="/r/FancyFollicles" rel="nofollow">/r/FancyFollicles</a><br>
<a href="/r/malehairadvice" rel="nofollow">/r/malehairadvice</a><br>
<a href="/r/curlyhair" rel="nofollow">/r/curlyhair</a> </p>
<h4 id="wiki_tattoos"><em>Tattoos</em></h4>
<p><a href="/r/tattoos" rel="nofollow">/r/tattoos</a><br>
<a href="/r/badtattoos" rel="nofollow">/r/badtattoos</a><br>
<a href="/r/tattoo" rel="nofollow">/r/tattoo</a> </p>
<h3 id="wiki_fashion"><em>Fashion</em></h3>
<p><a href="/r/malefashionadvice" rel="nofollow">/r/malefashionadvice</a><br>
<a href="/r/frugalmalefashion" rel="nofollow">/r/frugalmalefashion</a><br>
<a href="/r/femalefashionadvice" rel="nofollow">/r/femalefashionadvice</a><br>
<a href="/r/thriftstorehauls" rel="nofollow">/r/thriftstorehauls</a><br>
<a href="/r/fashion" rel="nofollow">/r/fashion</a><br>
<a href="/r/streetwear" rel="nofollow">/r/streetwear</a><br>
<a href="/r/malefashion" rel="nofollow">/r/malefashion</a><br>
<a href="/r/supremeclothing" rel="nofollow">/r/supremeclothing</a><br>
<a href="/r/FashionReps" rel="nofollow">/r/FashionReps</a> </p>
<h4 id="wiki_shoes"><em>Shoes</em></h4>
<p><a href="/r/sneakers" rel="nofollow">/r/sneakers</a><br>
<a href="/r/repsneakers" rel="nofollow">/r/repsneakers</a><br>
<a href="/r/goodyearwelt" rel="nofollow">/r/goodyearwelt</a> </p>
<h2 id="wiki_food"><strong>Food</strong></h2>
<p><a href="/r/food" rel="nofollow">/r/food</a><br>
<a href="/r/FoodPorn" rel="nofollow">/r/FoodPorn</a><br>
<a href="/r/foodhacks" rel="nofollow">/r/foodhacks</a><br>
<a href="/r/shittyfoodporn" rel="nofollow">/r/shittyfoodporn</a><br>
<a href="/r/eatsandwiches" rel="nofollow">/r/eatsandwiches</a><br>
<a href="/r/nutrition" rel="nofollow">/r/nutrition</a><br>
<a href="/r/mealtimevideos" rel="nofollow">/r/mealtimevideos</a><br>
<a href="/r/WeWantPlates" rel="nofollow">/r/WeWantPlates</a><br>
<a href="/r/forbiddensnacks" rel="nofollow">/r/forbiddensnacks</a><br>
<a href="/r/seriouseats" rel="nofollow">/r/seriouseats</a> </p>
<h3 id="wiki_cooking"><em>Cooking</em></h3>
<p><a href="/r/cooking" rel="nofollow">/r/cooking</a><br>
<a href="/r/slowcooking" rel="nofollow">/r/slowcooking</a><br>
<a href="/r/askculinary" rel="nofollow">/r/askculinary</a><br>
<a href="/r/baking" rel="nofollow">/r/baking</a><br>
<a href="/r/mealprepsunday" rel="nofollow">/r/mealprepsunday</a><br>
<a href="/r/breadit" rel="nofollow">/r/breadit</a><br>
<a href="/r/cookingforbeginners" rel="nofollow">/r/cookingforbeginners</a><br>
<a href="/r/smoking" rel="nofollow">/r/smoking</a><br>
<a href="/r/castiron" rel="nofollow">/r/castiron</a><br>
<a href="/r/instantpot" rel="nofollow">/r/instantpot</a> </p>
<h3 id="wiki_diets"><em>Diets</em></h3>
<p><a href="/r/EatCheapAndHealthy" rel="nofollow">/r/EatCheapAndHealthy</a><br>
<a href="/r/fitmeals" rel="nofollow">/r/fitmeals</a><br>
<a href="/r/budgetfood" rel="nofollow">/r/budgetfood</a><br>
<a href="/r/ketorecipes" rel="nofollow">/r/ketorecipes</a><br>
<a href="/r/vegan" rel="nofollow">/r/vegan</a><br>
<a href="/r/1200isplenty" rel="nofollow">/r/1200isplenty</a><br>
<a href="/r/Cheap_Meals" rel="nofollow">/r/Cheap_Meals</a><br>
<a href="/r/HealthyFood" rel="nofollow">/r/HealthyFood</a><br>
<a href="/r/veganrecipes" rel="nofollow">/r/veganrecipes</a><br>
<a href="/r/intermittentfasting" rel="nofollow">/r/intermittentfasting</a><br>
<a href="/r/fasting" rel="nofollow">/r/fasting</a> </p>
<h3 id="wiki_drinks_.28non-alcoholic.29"><em>Drinks (non-alcoholic)</em></h3>
<p><a href="/r/coffee" rel="nofollow">/r/coffee</a><br>
<a href="/r/tea" rel="nofollow">/r/tea</a> </p>
<h3 id="wiki_recipes"><em>Recipes</em></h3>
<p><a href="/r/recipes" rel="nofollow">/r/recipes</a><br>
<a href="/r/gifrecipes" rel="nofollow">/r/gifrecipes</a><br>
<a href="/r/veganrecipes" rel="nofollow">/r/veganrecipes</a> </p>
<h3 id="wiki_specific_food"><em>Specific food</em></h3>
<p><a href="/r/pizza" rel="nofollow">/r/pizza</a><br>
<a href="/r/grilledcheese" rel="nofollow">/r/grilledcheese</a><br>
<a href="/r/ramen" rel="nofollow">/r/ramen</a><br>
<a href="/r/bbq" rel="nofollow">/r/bbq</a><br>
<a href="/r/sushi" rel="nofollow">/r/sushi</a> </p>
<h2 id="wiki_money"><strong>Money</strong></h2>
<p><a href="/r/PersonalFinance" rel="nofollow">/r/PersonalFinance</a><br>
<a href="/r/Entrepreneur" rel="nofollow">/r/Entrepreneur</a><br>
<a href="/r/beermoney" rel="nofollow">/r/beermoney</a><br>
<a href="/r/startups" rel="nofollow">/r/startups</a><br>
<a href="/r/finance" rel="nofollow">/r/finance</a><br>
<a href="/r/economy" rel="nofollow">/r/economy</a><br>
<a href="/r/financialindependence" rel="nofollow">/r/financialindependence</a><br>
<a href="/r/apphookup" rel="nofollow">/r/apphookup</a><br>
<a href="/r/churning" rel="nofollow">/r/churning</a><br>
<a href="/r/realestate" rel="nofollow">/r/realestate</a><br>
<a href="/r/flipping" rel="nofollow">/r/flipping</a><br>
<a href="/r/antimlm" rel="nofollow">/r/antimlm</a><br>
<a href="/r/ripple" rel="nofollow">/r/ripple</a><br>
<a href="/r/Iota" rel="nofollow">/r/Iota</a><br>
<a href="/r/stellar" rel="nofollow">/r/stellar</a> </p>
<h3 id="wiki_betting.2Finvesting.2Fstocks"><em>Betting/Investing/Stocks</em></h3>
<p><a href="/r/investing" rel="nofollow">/r/investing</a><br>
<a href="/r/wallstreetbets" rel="nofollow">/r/wallstreetbets</a><br>
<a href="/r/millionairemakers" rel="nofollow">/r/millionairemakers</a><br>
<a href="/r/weedstocks" rel="nofollow">/r/weedstocks</a> </p>
<h3 id="wiki_budget"><em>Budget</em></h3>
<p><a href="/r/frugal" rel="nofollow">/r/frugal</a><br>
<a href="/r/EatCheapAndHealthy" rel="nofollow">/r/EatCheapAndHealthy</a><br>
<a href="/r/frugalmalefashion" rel="nofollow">/r/frugalmalefashion</a><br>
<a href="/r/budgetfood" rel="nofollow">/r/budgetfood</a><br>
<a href="/r/cheap_meals" rel="nofollow">/r/cheap_meals</a><br>
<a href="/r/Frugal_Jerk" rel="nofollow">/r/Frugal_Jerk</a><br>
<a href="/r/povertyfinance" rel="nofollow">/r/povertyfinance</a> </p>
<h3 id="wiki_consumerism"><em>Consumerism</em></h3>
<p><a href="/r/shutupandtakemymoney" rel="nofollow">/r/shutupandtakemymoney</a><br>
<a href="/r/BuyItForLife" rel="nofollow">/r/BuyItForLife</a><br>
<a href="/r/crappyoffbrands" rel="nofollow">/r/crappyoffbrands</a><br>
<a href="/r/shouldibuythisgame" rel="nofollow">/r/shouldibuythisgame</a><br>
<a href="/r/Anticonsumption" rel="nofollow">/r/Anticonsumption</a><br>
<a href="/r/sbubby" rel="nofollow">/r/sbubby</a><br>
<a href="/r/Wellworn" rel="nofollow">/r/Wellworn</a> </p>
<h3 id="wiki_cryptocurrency"><em>CryptoCurrency</em></h3>
<p><a href="/r/Bitcoin" rel="nofollow">/r/Bitcoin</a><br>
<a href="/r/dogecoin" rel="nofollow">/r/dogecoin</a><br>
<a href="/r/CryptoCurrency" rel="nofollow">/r/CryptoCurrency</a><br>
<a href="/r/ethereum" rel="nofollow">/r/ethereum</a><br>
<a href="/r/ethtrade" rel="nofollow">/r/ethtrade</a><br>
<a href="/r/litecoin" rel="nofollow">/r/litecoin</a><br>
<a href="/r/btc" rel="nofollow">/r/btc</a><br>
<a href="/r/garlicoin" rel="nofollow">/r/garlicoin</a><br>
<a href="/r/cardano" rel="nofollow">/r/cardano</a><br>
<a href="/r/Vechain" rel="nofollow">/r/Vechain</a> </p>
<h2 id="wiki_religion.2Fbeliefs"><strong>Religion/Beliefs</strong></h2>
<p><a href="/r/Psychonaut" rel="nofollow">/r/Psychonaut</a><br>
<a href="/r/Buddhism" rel="nofollow">/r/Buddhism</a><br>
<a href="/r/Stoicism" rel="nofollow">/r/Stoicism</a><br>
<a href="/r/occult" rel="nofollow">/r/occult</a> </p>
<h3 id="wiki_atheism"><em>Atheism</em></h3>
<p><a href="/r/atheism" rel="nofollow">/r/atheism</a><br>
<a href="/r/trueatheism" rel="nofollow">/r/trueatheism</a> </p>
<h3 id="wiki_christianity"><em>Christianity</em></h3>
<p><a href="/r/Christianity" rel="nofollow">/r/Christianity</a><br>
<a href="/r/dankchristianmemes" rel="nofollow">/r/dankchristianmemes</a><br>
<a href="/r/exmormon" rel="nofollow">/r/exmormon</a><br>
<a href="/r/Catholicism" rel="nofollow">/r/Catholicism</a> </p>
<h3 id="wiki_philosophy"><em>Philosophy</em></h3>
<p><a href="/r/philosophy" rel="nofollow">/r/philosophy</a><br>
<a href="/r/askphilosophy" rel="nofollow">/r/askphilosophy</a> </p>
<h2 id="wiki_relationships.2Fsex"><strong>Relationships/Sex</strong></h2>
<p><a href="/r/socialskills" rel="nofollow">/r/socialskills</a><br>
<a href="/r/socialengineering" rel="nofollow">/r/socialengineering</a><br>
<a href="/r/weddingplanning" rel="nofollow">/r/weddingplanning</a> </p>
<h3 id="wiki_family"><em>Family</em></h3>
<p><a href="/r/Parenting" rel="nofollow">/r/Parenting</a><br>
<a href="/r/childfree" rel="nofollow">/r/childfree</a><br>
<a href="/r/raisedbynarcissists" rel="nofollow">/r/raisedbynarcissists</a><br>
<a href="/r/incest" rel="nofollow">/r/incest</a><br>
<a href="/r/daddit" rel="nofollow">/r/daddit</a><br>
<a href="/r/justnomil" rel="nofollow">/r/justnomil</a><br>
<a href="/r/justnofamily" rel="nofollow">/r/justnofamily</a> </p>
<h3 id="wiki_relationships"><em>Relationships</em></h3>
<p><a href="/r/relationships" rel="nofollow">/r/relationships</a><br>
<a href="/r/relationship_advice" rel="nofollow">/r/relationship_advice</a><br>
<a href="/r/dating_advice" rel="nofollow">/r/dating_advice</a> </p>
<h4 id="wiki_online_relationships"><em>Online Relationships</em></h4>
<p><a href="/r/Tinder" rel="nofollow">/r/Tinder</a><br>
<a href="/r/OKCupid" rel="nofollow">/r/OKCupid</a><br>
<a href="/r/r4r" rel="nofollow">/r/r4r</a><br>
<a href="/r/dirtyr4r" rel="nofollow">/r/dirtyr4r</a> (NSFW)<br>
<a href="/r/longdistance" rel="nofollow">/r/longdistance</a> </p>
<h3 id="wiki_sex"><em>Sex</em></h3>
<p><a href="/r/sex" rel="nofollow">/r/sex</a><br>
<a href="/r/seduction" rel="nofollow">/r/seduction</a><br>
<a href="/r/nofap" rel="nofollow">/r/nofap</a><br>
<a href="/r/deadbedrooms" rel="nofollow">/r/deadbedrooms</a><br>
<a href="/r/polyamory" rel="nofollow">/r/polyamory</a> </p>
<h2 id="wiki_self-improvement"><strong>Self-Improvement</strong></h2>
<p><a href="/r/GetMotivated" rel="nofollow">/r/GetMotivated</a><br>
<a href="/r/QuotesPorn" rel="nofollow">/r/QuotesPorn</a><br>
<a href="/r/getdisciplined" rel="nofollow">/r/getdisciplined</a><br>
<a href="/r/happy" rel="nofollow">/r/happy</a><br>
<a href="/r/productivity" rel="nofollow">/r/productivity</a><br>
<a href="/r/DecidingToBeBetter" rel="nofollow">/r/DecidingToBeBetter</a><br>
<a href="/r/mademesmile" rel="nofollow">/r/mademesmile</a><br>
<a href="/r/selfimprovement" rel="nofollow">/r/selfimprovement</a><br>
<a href="/r/iwantout" rel="nofollow">/r/iwantout</a><br>
<a href="/r/humansbeingbros" rel="nofollow">/r/humansbeingbros</a><br>
<a href="/r/happycrowds" rel="nofollow">/r/happycrowds</a><br>
<a href="/r/sportsarefun" rel="nofollow">/r/sportsarefun</a><br>
<a href="/r/GetStudying" rel="nofollow">/r/GetStudying</a> </p>
<hr>
<h1 id="wiki_technology"><strong>Technology</strong></h1>
<p>More tech related subreddits, from the sidebar of <a href="/r/technology" rel="nofollow">/r/technology</a>, can be found <a href="http://www.reddit.com/r/ListOfSubreddits/wiki/technology" rel="nofollow">here.</a></p>
<p><a href="/r/technology" rel="nofollow">/r/technology</a><br>
<a href="/r/internetisbeautiful" rel="nofollow">/r/internetisbeautiful</a><br>
<a href="/r/futurology" rel="nofollow">/r/futurology</a><br>
<a href="/r/pcmasterrace" rel="nofollow">/r/pcmasterrace</a><br>
<a href="/r/buildapc" rel="nofollow">/r/buildapc</a><br>
<a href="/r/talesfromtechsupport" rel="nofollow">/r/talesfromtechsupport</a><br>
<a href="/r/netsec" rel="nofollow">/r/netsec</a><br>
<a href="/r/gamedev" rel="nofollow">/r/gamedev</a><br>
<a href="/r/design" rel="nofollow">/r/design</a><br>
<a href="/r/engineering" rel="nofollow">/r/engineering</a><br>
<a href="/r/jailbreak" rel="nofollow">/r/jailbreak</a><br>
<a href="/r/compsci" rel="nofollow">/r/compsci</a><br>
<a href="/r/tech" rel="nofollow">/r/tech</a><br>
<a href="/r/hacking" rel="nofollow">/r/hacking</a><br>
<a href="/r/imaginarytechnology" rel="nofollow">/r/imaginarytechnology</a><br>
<a href="/r/privacy" rel="nofollow">/r/privacy</a><br>
<a href="/r/torrents" rel="nofollow">/r/torrents</a><br>
<a href="/r/networking" rel="nofollow">/r/networking</a><br>
<a href="/r/infographics" rel="nofollow">/r/infographics</a><br>
<a href="/r/piracy" rel="nofollow">/r/piracy</a><br>
<a href="/r/EngineeringPorn" rel="nofollow">/r/EngineeringPorn</a><br>
<a href="/r/cableporn" rel="nofollow">/r/cableporn</a><br>
<a href="/r/simulated" rel="nofollow">/r/simulated</a><br>
<a href="/r/onions" rel="nofollow">/r/onions</a><br>
<a href="/r/unixporn" rel="nofollow">/r/unixporn</a><br>
<a href="/r/crackwatch" rel="nofollow">/r/crackwatch</a><br>
<a href="/r/php" rel="nofollow">/r/php</a><br>
<a href="/r/aboringdystopia" rel="nofollow">/r/aboringdystopia</a><br>
<a href="/r/virtualreality" rel="nofollow">/r/virtualreality</a><br>
<a href="/r/opensource" rel="nofollow">/r/opensource</a> </p>
<h2 id="wiki_3d_printing"><em>3D Printing</em></h2>
<p><a href="/r/3Dprinting" rel="nofollow">/r/3Dprinting</a><br>
<a href="/r/functionalprint" rel="nofollow">/r/functionalprint</a> </p>
<h2 id="wiki_business_tech"><em>Business Tech</em></h2>
<p><a href="/r/nintendo" rel="nofollow">/r/nintendo</a><br>
<a href="/r/spacex" rel="nofollow">/r/spacex</a><br>
<a href="/r/nasa" rel="nofollow">/r/nasa</a><br>
<a href="/r/amd" rel="nofollow">/r/amd</a><br>
<a href="/r/nvidia" rel="nofollow">/r/nvidia</a><br>
<a href="/r/photoshop" rel="nofollow">/r/photoshop</a><br>
<a href="/r/firefox" rel="nofollow">/r/firefox</a> </p>
<h3 id="wiki_android_products"><em>Android products</em></h3>
<p><a href="/r/Android" rel="nofollow">/r/Android</a><br>
<a href="/r/AndroidApps" rel="nofollow">/r/AndroidApps</a><br>
<a href="/r/AndroidGaming" rel="nofollow">/r/AndroidGaming</a><br>
<a href="/r/AndroidDev" rel="nofollow">/r/AndroidDev</a><br>
<a href="/r/AndroidThemes" rel="nofollow">/r/AndroidThemes</a><br>
<a href="/r/oneplus" rel="nofollow">/r/oneplus</a> </p>
<h3 id="wiki_apple_products"><em>Apple Products</em></h3>
<p><a href="/r/apple" rel="nofollow">/r/apple</a><br>
<a href="/r/iphone" rel="nofollow">/r/iphone</a><br>
<a href="/r/mac" rel="nofollow">/r/mac</a><br>
<a href="/r/ipad" rel="nofollow">/r/ipad</a><br>
<a href="/r/applewatch" rel="nofollow">/r/applewatch</a> </p>
<h3 id="wiki_gadgets"><em>Gadgets</em></h3>
<p><a href="/r/gadgets" rel="nofollow">/r/gadgets</a><br>
<a href="/r/raspberry_pi" rel="nofollow">/r/raspberry_pi</a><br>
<a href="/r/electronics" rel="nofollow">/r/electronics</a><br>
<a href="/r/arduino" rel="nofollow">/r/arduino</a><br>
<a href="/r/trackers" rel="nofollow">/r/trackers</a><br>
<a href="/r/gopro" rel="nofollow">/r/gopro</a><br>
<a href="/r/blender" rel="nofollow">/r/blender</a><br>
<a href="/r/amazonecho" rel="nofollow">/r/amazonecho</a><br>
<a href="/r/RetroPie" rel="nofollow">/r/RetroPie</a> </p>
<h4 id="wiki_hardware"><em>Hardware</em></h4>
<p><a href="/r/hardware" rel="nofollow">/r/hardware</a><br>
<a href="/r/hardwareswap" rel="nofollow">/r/hardwareswap</a> </p>
<h4 id="wiki_kodi"><em>Kodi</em></h4>
<p><a href="/r/Addons4Kodi" rel="nofollow">/r/Addons4Kodi</a><br>
<a href="/r/kodi" rel="nofollow">/r/kodi</a> </p>
<h3 id="wiki_google_products"><em>Google Products</em></h3>
<p><a href="/r/google" rel="nofollow">/r/google</a><br>
<a href="/r/chromecast" rel="nofollow">/r/chromecast</a><br>
<a href="/r/googlepixel" rel="nofollow">/r/googlepixel</a><br>
<a href="/r/googlehome" rel="nofollow">/r/googlehome</a> </p>
<h3 id="wiki_linux"><em>Linux</em></h3>
<p><a href="/r/linux" rel="nofollow">/r/linux</a><br>
<a href="/r/linux_gaming" rel="nofollow">/r/linux_gaming</a><br>
<a href="/r/linux4noobs" rel="nofollow">/r/linux4noobs</a><br>
<a href="/r/linuxmasterrace" rel="nofollow">/r/linuxmasterrace</a><br>
<a href="/r/archlinux" rel="nofollow">/r/archlinux</a> </p>
<h3 id="wiki_microsoft_products"><em>Microsoft Products</em></h3>
<p><a href="/r/Windows10" rel="nofollow">/r/Windows10</a><br>
<a href="/r/windows" rel="nofollow">/r/windows</a><br>
<a href="/r/excel" rel="nofollow">/r/excel</a><br>
<a href="/r/surface" rel="nofollow">/r/surface</a><br>
<a href="/r/microsoft" rel="nofollow">/r/microsoft</a> </p>
<h2 id="wiki_data"><em>Data</em></h2>
<p><a href="/r/dataisbeautiful" rel="nofollow">/r/dataisbeautiful</a><br>
<a href="/r/DataHoarder" rel="nofollow">/r/DataHoarder</a> </p>
<h2 id="wiki_digital_currency"><em>Digital Currency</em></h2>
<p><a href="/r/Bitcoin" rel="nofollow">/r/Bitcoin</a><br>
<a href="/r/dogecoin" rel="nofollow">/r/dogecoin</a><br>
<a href="/r/CryptoCurrency" rel="nofollow">/r/CryptoCurrency</a><br>
<a href="/r/ethereum" rel="nofollow">/r/ethereum</a><br>
<a href="/r/ethtrader" rel="nofollow">/r/ethtrader</a><br>
<a href="/r/btc" rel="nofollow">/r/btc</a><br>
<a href="/r/litecoin" rel="nofollow">/r/litecoin</a><br>
<a href="/r/bitcoinmarkets" rel="nofollow">/r/bitcoinmarkets</a><br>
<a href="/r/cryptomarkets" rel="nofollow">/r/cryptomarkets</a><br>
<a href="/r/monero" rel="nofollow">/r/monero</a><br>
<a href="/r/neo" rel="nofollow">/r/neo</a> </p>
<h2 id="wiki_programming"><em>Programming</em></h2>
<p><a href="/r/programming" rel="nofollow">/r/programming</a><br>
<a href="/r/learnprogramming" rel="nofollow">/r/learnprogramming</a><br>
<a href="/r/python" rel="nofollow">/r/python</a><br>
<a href="/r/java" rel="nofollow">/r/java</a><br>
<a href="/r/javascript" rel="nofollow">/r/javascript</a><br>
<a href="/r/learnpython" rel="nofollow">/r/learnpython</a><br>
<a href="/r/excel" rel="nofollow">/r/excel</a><br>
<a href="/r/unity3d" rel="nofollow">/r/unity3d</a> </p>
<h2 id="wiki_sound"><em>Sound</em></h2>
<p><a href="/r/audiophile" rel="nofollow">/r/audiophile</a><br>
<a href="/r/headphones" rel="nofollow">/r/headphones</a><br>
<a href="/r/audioengineering" rel="nofollow">/r/audioengineering</a> </p>
<hr>
<h1 id="wiki_humor"><strong>Humor</strong></h1>
<h2 id="wiki_general_humor"><strong>General Humor</strong></h2>
<p><a href="/r/funny" rel="nofollow">/r/funny</a><br>
<a href="/r/humor" rel="nofollow">/r/humor</a><br>
<a href="/r/contagiouslaughter" rel="nofollow">/r/contagiouslaughter</a><br>
<a href="/r/standupcomedy" rel="nofollow">/r/standupcomedy</a><br>
<a href="/r/ProgrammerHumor" rel="nofollow">/r/ProgrammerHumor</a><br>
<a href="/r/prematurecelebration" rel="nofollow">/r/prematurecelebration</a><br>
<a href="/r/ChildrenFallingOver" rel="nofollow">/r/ChildrenFallingOver</a><br>
<a href="/r/dadreflexes" rel="nofollow">/r/dadreflexes</a><br>
<a href="/r/kenm" rel="nofollow">/r/kenm</a><br>
<a href="/r/politicalhumor" rel="nofollow">/r/politicalhumor</a><br>
<a href="/r/accidentalcomedy" rel="nofollow">/r/accidentalcomedy</a><br>
<a href="/r/ComedyCemetery" rel="nofollow">/r/ComedyCemetery</a><br>
<a href="/r/funnyandsad" rel="nofollow">/r/funnyandsad</a><br>
<a href="/r/kidsarefuckingstupid" rel="nofollow">/r/kidsarefuckingstupid</a><br>
<a href="/r/notkenm" rel="nofollow">/r/notkenm</a><br>
<a href="/r/comedyheaven" rel="nofollow">/r/comedyheaven</a><br>
<a href="/r/comedynecromancy" rel="nofollow">/r/comedynecromancy</a><br>
<a href="/r/comedyhomicide" rel="nofollow">/r/comedyhomicide</a> </p>
<h3 id="wiki_jokes"><em>Jokes</em></h3>
<p><strong><a href="/r/Jokes" rel="nofollow">/r/Jokes</a></strong><br>
<a href="/r/dadjokes" rel="nofollow">/r/dadjokes</a><br>
<a href="/r/standupshots" rel="nofollow">/r/standupshots</a><br>
<a href="/r/punny" rel="nofollow">/r/punny</a><br>
<a href="/r/antijokes" rel="nofollow">/r/antijokes</a><br>
<a href="/r/meanjokes" rel="nofollow">/r/meanjokes</a><br>
<a href="/r/3amjokes" rel="nofollow">/r/3amjokes</a><br>
<a href="/r/puns" rel="nofollow">/r/puns</a><br>
<a href="/r/WordAvalanches" rel="nofollow">/r/WordAvalanches</a><br>
<a href="/r/darkjokes" rel="nofollow">/r/darkjokes</a> </p>
<h2 id="wiki_memes.2Frage_comics"><strong>Memes/Rage comics</strong></h2>
<p><a href="/r/Demotivational" rel="nofollow">/r/Demotivational</a><br>
<a href="/r/lolcats" rel="nofollow">/r/lolcats</a><br>
<a href="/r/supershibe" rel="nofollow">/r/supershibe</a><br>
<a href="/r/copypasta" rel="nofollow">/r/copypasta</a><br>
<a href="/r/emojipasta" rel="nofollow">/r/emojipasta</a> </p>
<h3 id="wiki_memes_and_rage_comics"><em>Memes and Rage Comics</em></h3>
<p><a href="/r/TrollXChromosomes" rel="nofollow">/r/TrollXChromosomes</a><br>
<a href="/r/trollychromosome" rel="nofollow">/r/trollychromosome</a><br>
<a href="/r/starterpacks" rel="nofollow">/r/starterpacks</a> </p>
<h3 id="wiki_memes"><em>Memes</em></h3>
<p><a href="/r/AdviceAnimals" rel="nofollow">/r/AdviceAnimals</a><br>
<a href="/r/memes" rel="nofollow">/r/memes</a><br>
<a href="/r/trippinthroughtime" rel="nofollow">/r/trippinthroughtime</a><br>
<a href="/r/BikiniBottomTwitter" rel="nofollow">/r/BikiniBottomTwitter</a><br>
<a href="/r/dankmemes" rel="nofollow">/r/dankmemes</a><br>
<a href="/r/madlads" rel="nofollow">/r/madlads</a><br>
<a href="/r/bidenbro" rel="nofollow">/r/bidenbro</a><br>
<a href="/r/memeeconomy" rel="nofollow">/r/memeeconomy</a><br>
<a href="/r/rarepuppers" rel="nofollow">/r/rarepuppers</a><br>
<a href="/r/wholesomememes" rel="nofollow">/r/wholesomememes</a><br>
<a href="/r/dankchristianmemes" rel="nofollow">/r/dankchristianmemes</a><br>
<a href="/r/terriblefacebookmemes" rel="nofollow">/r/terriblefacebookmemes</a><br>
<a href="/r/prequelmemes" rel="nofollow">/r/prequelmemes</a><br>
<a href="/r/dank_meme" rel="nofollow">/r/dank_meme</a><br>
<a href="/r/trebuchetmemes" rel="nofollow">/r/trebuchetmemes</a><br>
<a href="/r/deepfriedmemes" rel="nofollow">/r/deepfriedmemes</a><br>
<a href="/r/Overwatch_Memes" rel="nofollow">/r/Overwatch_Memes</a><br>
<a href="/r/see" rel="nofollow">/r/see</a><br>
<a href="/r/SequelMemes" rel="nofollow">/r/SequelMemes</a><br>
<a href="/r/surrealmemes" rel="nofollow">/r/surrealmemes</a><br>
<a href="/r/bonehurtingjuice" rel="nofollow">/r/bonehurtingjuice</a><br>
<a href="/r/bossfight" rel="nofollow">/r/bossfight</a><br>
<a href="/r/historymemes" rel="nofollow">/r/historymemes</a><br>
<a href="/r/animemes" rel="nofollow">/r/animemes</a><br>
<a href="/r/suddenlygay" rel="nofollow">/r/suddenlygay</a><br>
<a href="/r/absoluteunits" rel="nofollow">/r/absoluteunits</a><br>
<a href="/r/delightfullychubby" rel="nofollow">/r/delightfullychubby</a><br>
<a href="/r/Memes_Of_The_Dank" rel="nofollow">/r/Memes_Of_The_Dank</a><br>
<a href="/r/smoobypost" rel="nofollow">/r/smoobypost</a><br>
<a href="/r/lotrmemes" rel="nofollow">/r/lotrmemes</a><br>
<a href="/r/ilikthebred" rel="nofollow">/r/ilikthebred</a><br>
<a href="/r/meme" rel="nofollow">/r/meme</a><br>
<a href="/r/garlicbreadmemes" rel="nofollow">/r/garlicbreadmemes</a><br>
<a href="/r/offensivememes" rel="nofollow">/r/offensivememes</a><br>
<a href="/r/gocommitdie" rel="nofollow">/r/gocommitdie</a><br>
<a href="/r/wholesomegreentext" rel="nofollow">/r/wholesomegreentext</a><br>
<a href="/r/raimememes" rel="nofollow">/r/raimememes</a><br>
<a href="/r/otmemes" rel="nofollow">/r/otmemes</a><br>
<a href="/r/kappa" rel="nofollow">/r/kappa</a><br>
<a href="/r/equelmemes" rel="nofollow">/r/equelmemes</a><br>
<a href="/r/namflashbacks" rel="nofollow">/r/namflashbacks</a> </p>
<h4 id="wiki_____irl"><em>____irl</em></h4>
<p><a href="/r/me_irl" rel="nofollow">/r/me_irl</a><br>
<a href="/r/meirl" rel="nofollow">/r/meirl</a><br>
<a href="/r/anime_irl" rel="nofollow">/r/anime_irl</a><br>
<a href="/r/2meirl4meirl" rel="nofollow">/r/2meirl4meirl</a><br>
<a href="/r/meow_irl" rel="nofollow">/r/meow_irl</a><br>
<a href="/r/woof_irl" rel="nofollow">/r/woof_irl</a><br>
<a href="/r/TooMeIrlForMeIrl" rel="nofollow">/r/TooMeIrlForMeIrl</a><br>
<a href="/r/absolutelynotme_irl" rel="nofollow">/r/absolutelynotme_irl</a><br>
<a href="/r/absolutelynotmeirl" rel="nofollow">/r/absolutelynotmeirl</a> </p>
<h3 id="wiki_rage_comics"><em>Rage Comics</em></h3>
<p><a href="/r/fffffffuuuuuuuuuuuu" rel="nofollow">/r/fffffffuuuuuuuuuuuu</a>
<a href="/r/iiiiiiitttttttttttt" rel="nofollow">/r/iiiiiiitttttttttttt</a> </p>
<hr>
<h1 id="wiki_other"><strong>Other</strong></h1>
<h2 id="wiki_animals"><strong>Animals</strong></h2>
<p><a href="http://www.reddit.com/r/AnimalReddits/wiki/faq" rel="nofollow">More here!</a> From <a href="/r/AnimalReddits" rel="nofollow">/r/AnimalReddits</a>.<br>
Note that not all of those are active.</p>
<p><a href="/r/AnimalsBeingJerks" rel="nofollow">/r/AnimalsBeingJerks</a> (see also <a href="http://www.reddit.com/r/ListOfSubreddits/wiki/being" rel="nofollow">The Being Network</a> )<br>
<a href="/r/AnimalsBeingBros" rel="nofollow">/r/AnimalsBeingBros</a><br>
<a href="/r/AnimalPorn" rel="nofollow">/r/AnimalPorn</a><br>
<a href="/r/AnimalsBeingDerps" rel="nofollow">/r/AnimalsBeingDerps</a><br>
<a href="/r/likeus" rel="nofollow">/r/likeus</a><br>
<a href="/r/stoppedworking" rel="nofollow">/r/stoppedworking</a><br>
<a href="/r/hitmanimals" rel="nofollow">/r/hitmanimals</a><br>
<a href="/r/animaltextgifs" rel="nofollow">/r/animaltextgifs</a><br>
<a href="/r/BeforeNAfterAdoption" rel="nofollow">/r/BeforeNAfterAdoption</a><br>
<a href="/r/sneks" rel="nofollow">/r/sneks</a><br>
<a href="/r/TsundereSharks" rel="nofollow">/r/TsundereSharks</a><br>
<a href="/r/whatsthisbug" rel="nofollow">/r/whatsthisbug</a><br>
<a href="/r/HybridAnimals" rel="nofollow">/r/HybridAnimals</a><br>
<a href="/r/zoomies" rel="nofollow">/r/zoomies</a><br>
<a href="/r/brushybrushy" rel="nofollow">/r/brushybrushy</a><br>
<a href="/r/bigboye" rel="nofollow">/r/bigboye</a><br>
<a href="/r/curledfeetsies" rel="nofollow">/r/curledfeetsies</a><br>
<a href="/r/mlem" rel="nofollow">/r/mlem</a><br>
<a href="/r/Floof" rel="nofollow">/r/Floof</a><br>
<a href="/r/shittyanimalfacts" rel="nofollow">/r/shittyanimalfacts</a><br>
<a href="/r/animalsthatlovemagic" rel="nofollow">/r/animalsthatlovemagic</a><br>
<a href="/r/spiderbro" rel="nofollow">/r/spiderbro</a><br>
<a href="/r/properanimalnames" rel="nofollow">/r/properanimalnames</a> </p>
<h3 id="wiki_birds"><em>Birds</em></h3>
<p><a href="/r/birdswitharms" rel="nofollow">/r/birdswitharms</a><br>
<a href="/r/superbowl" rel="nofollow">/r/superbowl</a><br>
<a href="/r/birbs" rel="nofollow">/r/birbs</a><br>
<a href="/r/partyparrot" rel="nofollow">/r/partyparrot</a><br>
<a href="/r/birdsbeingdicks" rel="nofollow">/r/birdsbeingdicks</a><br>
<a href="/r/emuwarflashbacks" rel="nofollow">/r/emuwarflashbacks</a> </p>
<h3 id="wiki_mammals"><em>Mammals</em></h3>
<p><a href="/r/babyelephantgifs" rel="nofollow">/r/babyelephantgifs</a><br>
<a href="/r/sloths" rel="nofollow">/r/sloths</a><br>
<a href="/r/foxes" rel="nofollow">/r/foxes</a><br>
<a href="/r/trashpandas" rel="nofollow">/r/trashpandas</a><br>
<a href="/r/happycowgifs" rel="nofollow">/r/happycowgifs</a><br>
<a href="/r/rabbits" rel="nofollow">/r/rabbits</a><br>
<a href="/r/goatparkour" rel="nofollow">/r/goatparkour</a> </p>
<h4 id="wiki_cats"><em>Cats</em></h4>
<p><a href="/r/cats" rel="nofollow">/r/cats</a> (more <a href="http://www.reddit.com/r/Catsubs/wiki/index" rel="nofollow">here</a> from <a href="/r/CatSubs" rel="nofollow">/r/CatSubs</a>)<br>
<a href="/r/startledcats" rel="nofollow">/r/startledcats</a><br>
<a href="/r/catpictures" rel="nofollow">/r/catpictures</a><br>
<a href="/r/catsstandingup" rel="nofollow">/r/catsstandingup</a><br>
<a href="/r/catpranks" rel="nofollow">/r/catpranks</a><br>
<a href="/r/meow_irl" rel="nofollow">/r/meow_irl</a><br>
<a href="/r/holdmycatnip" rel="nofollow">/r/holdmycatnip</a><br>
<a href="/r/catslaps" rel="nofollow">/r/catslaps</a><br>
<a href="/r/thecatdimension" rel="nofollow">/r/thecatdimension</a><br>
<a href="/r/babybigcatgifs" rel="nofollow">/r/babybigcatgifs</a><br>
<a href="/r/catloaf" rel="nofollow">/r/catloaf</a><br>
<a href="/r/thisismylifemeow" rel="nofollow">/r/thisismylifemeow</a><br>
<a href="/r/cattaps" rel="nofollow">/r/cattaps</a><br>
<a href="/r/teefies" rel="nofollow">/r/teefies</a><br>
<a href="/r/tuckedinkitties" rel="nofollow">/r/tuckedinkitties</a><br>
<a href="/r/catsareassholes" rel="nofollow">/r/catsareassholes</a><br>
<a href="/r/catsisuottatfo" rel="nofollow">/r/catsisuottatfo</a><br>
<a href="/r/stuffoncats" rel="nofollow">/r/stuffoncats</a><br>
<a href="/r/bigcatgifs" rel="nofollow">/r/bigcatgifs</a><br>
<a href="/r/jellybeantoes" rel="nofollow">/r/jellybeantoes</a><br>
<a href="/r/catsareliquid" rel="nofollow">/r/catsareliquid</a><br>
<a href="/r/catgifs" rel="nofollow">/r/catgifs</a><br>
<a href="/r/blackcats" rel="nofollow">/r/blackcats</a><br>
<a href="/r/supermodelcats" rel="nofollow">/r/supermodelcats</a> </p>
<h4 id="wiki_dogs"><em>Dogs</em></h4>
<p><a href="/r/dogs" rel="nofollow">/r/dogs</a><br>
<a href="/r/dogpictures" rel="nofollow">/r/dogpictures</a><br>
<a href="/r/dogtraining" rel="nofollow">/r/dogtraining</a><br>
<a href="/r/woof_irl" rel="nofollow">/r/woof_irl</a><br>
<a href="/r/WhatsWrongWithYourDog" rel="nofollow">/r/WhatsWrongWithYourDog</a><br>
<a href="/r/dogberg" rel="nofollow">/r/dogberg</a><br>
<a href="/r/dogswithjobs" rel="nofollow">/r/dogswithjobs</a><br>
<a href="/r/masterreturns" rel="nofollow">/r/masterreturns</a><br>
<a href="/r/barkour" rel="nofollow">/r/barkour</a><br>
<a href="/r/blop" rel="nofollow">/r/blop</a><br>
<a href="/r/puppysmiles" rel="nofollow">/r/puppysmiles</a><br>
<a href="/r/puppies" rel="nofollow">/r/puppies</a><br>
<a href="/r/petthedamndog" rel="nofollow">/r/petthedamndog</a> </p>
<h5 id="wiki_breeds"><em>Breeds</em></h5>
<p><a href="/r/corgi" rel="nofollow">/r/corgi</a><br>
<a href="/r/Pitbulls" rel="nofollow">/r/Pitbulls</a><br>
<a href="/r/goldenretrievers" rel="nofollow">/r/goldenretrievers</a><br>
<a href="/r/incorgnito" rel="nofollow">/r/incorgnito</a><br>
<a href="/r/babycorgis" rel="nofollow">/r/babycorgis</a> </p>
<h2 id="wiki_conspiracy"><strong>Conspiracy</strong></h2>
<p><a href="/r/conspiracy" rel="nofollow">/r/conspiracy</a><br>
<a href="/r/skeptic" rel="nofollow">/r/skeptic</a><br>
<a href="/r/karmaconspiracy" rel="nofollow">/r/karmaconspiracy</a><br>
<a href="/r/UFOs" rel="nofollow">/r/UFOs</a><br>
<a href="/r/conspiratard" rel="nofollow">/r/conspiratard</a><br>
<a href="/r/empiredidnothingwrong" rel="nofollow">/r/empiredidnothingwrong</a><br>
<a href="/r/scp" rel="nofollow">/r/scp</a> </p>
<h2 id="wiki_cringe"><strong>Cringe</strong></h2>
<p><a href="/r/cringepics" rel="nofollow">/r/cringepics</a><br>
<a href="/r/cringe" rel="nofollow">/r/cringe</a><br>
<a href="/r/instant_regret" rel="nofollow">/r/instant_regret</a><br>
<a href="/r/blunderyears" rel="nofollow">/r/blunderyears</a><br>
<a href="/r/facepalm" rel="nofollow">/r/facepalm</a><br>
<a href="/r/fatlogic" rel="nofollow">/r/fatlogic</a><br>
<a href="/r/publicfreakout" rel="nofollow">/r/publicfreakout</a><br>
<a href="/r/lewronggeneration" rel="nofollow">/r/lewronggeneration</a><br>
<a href="/r/fellowkids" rel="nofollow">/r/fellowkids</a><br>
<a href="/r/sadcringe" rel="nofollow">/r/sadcringe</a><br>
<a href="/r/corporatefacepalm" rel="nofollow">/r/corporatefacepalm</a><br>
<a href="/r/4PanelCringe" rel="nofollow">/r/4PanelCringe</a><br>
<a href="/r/amibeingdetained" rel="nofollow">/r/amibeingdetained</a><br>
<a href="/r/instantbarbarians" rel="nofollow">/r/instantbarbarians</a><br>
<a href="/r/watchpeopledieinside" rel="nofollow">/r/watchpeopledieinside</a><br>
<a href="/r/technicallythetruth" rel="nofollow">/r/technicallythetruth</a><br>
<a href="/r/accidentalracism" rel="nofollow">/r/accidentalracism</a><br>
<a href="/r/engrish" rel="nofollow">/r/engrish</a><br>
<a href="/r/wokekids" rel="nofollow">/r/wokekids</a><br>
<a href="/r/masterhacker" rel="nofollow">/r/masterhacker</a> </p>
<h3 id="wiki_called_out"><em>Called out</em></h3>
<p><a href="/r/facepalm" rel="nofollow">/r/facepalm</a><br>
<a href="/r/quityourbullshit" rel="nofollow">/r/quityourbullshit</a><br>
<a href="/r/thathappened" rel="nofollow">/r/thathappened</a><br>
<a href="/r/delusionalartists" rel="nofollow">/r/delusionalartists</a><br>
<a href="/r/oopsdidntmeanto" rel="nofollow">/r/oopsdidntmeanto</a><br>
<a href="/r/beholdthemasterrace" rel="nofollow">/r/beholdthemasterrace</a><br>
<a href="/r/murderedbywords" rel="nofollow">/r/murderedbywords</a><br>
<a href="/r/ihavesex" rel="nofollow">/r/ihavesex</a><br>
<a href="/r/woooosh" rel="nofollow">/r/woooosh</a><br>
<a href="/r/badfaketexts" rel="nofollow">/r/badfaketexts</a><br>
<a href="/r/boneappletea" rel="nofollow">/r/boneappletea</a><br>
<a href="/r/atetheonion" rel="nofollow">/r/atetheonion</a><br>
<a href="/r/iamatotalpieceofshit" rel="nofollow">/r/iamatotalpieceofshit</a><br>
<a href="/r/suicidebywords" rel="nofollow">/r/suicidebywords</a><br>
<a href="/r/wowthanksimcured" rel="nofollow">/r/wowthanksimcured</a><br>
<a href="/r/topmindsofreddit" rel="nofollow">/r/topmindsofreddit</a><br>
<a href="/r/lostredditors" rel="nofollow">/r/lostredditors</a><br>
<a href="/r/dontyouknowwhoiam" rel="nofollow">/r/dontyouknowwhoiam</a><br>
<a href="/r/NobodyAsked" rel="nofollow">/r/NobodyAsked</a><br>
<a href="/r/dontfundme" rel="nofollow">/r/dontfundme</a><br>
<a href="/r/nothingeverhappens" rel="nofollow">/r/nothingeverhappens</a><br>
<a href="/r/vaxxhappened" rel="nofollow">/r/vaxxhappened</a><br>
<a href="/r/goodfaketexts" rel="nofollow">/r/goodfaketexts</a><br>
<a href="/r/delusionalcraigslist" rel="nofollow">/r/delusionalcraigslist</a><br>
<a href="/r/suspiciousquotes" rel="nofollow">/r/suspiciousquotes</a><br>
<a href="/r/facingtheirparenting" rel="nofollow">/r/facingtheirparenting</a><br>
<a href="/r/ihadastroke" rel="nofollow">/r/ihadastroke</a><br>
<a href="/r/untrustworthypoptarts" rel="nofollow">/r/untrustworthypoptarts</a><br>
<a href="/r/phonesarebad" rel="nofollow">/r/phonesarebad</a> </p>
<h3 id="wiki_.22neckbeard.22"><em>"Neckbeard"</em></h3>
<p><a href="/r/niceguys" rel="nofollow">/r/niceguys</a><br>
<a href="/r/iamverysmart" rel="nofollow">/r/iamverysmart</a><br>
<a href="/r/justneckbeardthings" rel="nofollow">/r/justneckbeardthings</a><br>
<a href="/r/iamverybadass" rel="nofollow">/r/iamverybadass</a><br>
<a href="/r/mallninjashit" rel="nofollow">/r/mallninjashit</a><br>
<a href="/r/ChoosingBeggars" rel="nofollow">/r/ChoosingBeggars</a><br>
<a href="/r/gatekeeping" rel="nofollow">/r/gatekeeping</a><br>
<a href="/r/nicegirls" rel="nofollow">/r/nicegirls</a><br>
<a href="/r/creepyasterisks" rel="nofollow">/r/creepyasterisks</a><br>
<a href="/r/inceltears" rel="nofollow">/r/inceltears</a><br>
<a href="/r/humblebrag" rel="nofollow">/r/humblebrag</a><br>
<a href="/r/nothowdrugswork" rel="nofollow">/r/nothowdrugswork</a><br>
<a href="/r/neckbeardnests" rel="nofollow">/r/neckbeardnests</a><br>
<a href="/r/whiteknighting" rel="nofollow">/r/whiteknighting</a><br>
<a href="/r/neckbeardrpg" rel="nofollow">/r/neckbeardrpg</a> </p>
<h2 id="wiki_cute"><strong>Cute</strong></h2>
<p><a href="/r/aww" rel="nofollow">/r/aww</a><br>
<a href="/r/cats" rel="nofollow">/r/cats</a><br>
<a href="/r/animalsbeingjerks" rel="nofollow">/r/animalsbeingjerks</a><br>
<a href="/r/animalsbeingbros" rel="nofollow">/r/animalsbeingbros</a><br>
<a href="/r/Awwducational" rel="nofollow">/r/Awwducational</a><br>
<a href="/r/dogs" rel="nofollow">/r/dogs</a><br>
<a href="/r/corgi" rel="nofollow">/r/corgi</a><br>
<a href="/r/thisismylifenow" rel="nofollow">/r/thisismylifenow</a><br>
<a href="/r/blep" rel="nofollow">/r/blep</a><br>
<a href="/r/eyebeach" rel="nofollow">/r/eyebeach</a><br>
<a href="/r/tippytaps" rel="nofollow">/r/tippytaps</a><br>
<a href="/r/awww" rel="nofollow">/r/awww</a><br>
<a href="/r/babycorgis" rel="nofollow">/r/babycorgis</a> </p>
<h2 id="wiki_disgusting.2Fangering.2Fscary.2Fweird_.28note.3A_potentially_nsfl.29"><strong>Disgusting/Angering/Scary/Weird</strong> (Note: Potentially NSFL)</h2>
<p><strong><a href="/r/WTF" rel="nofollow">/r/WTF</a></strong><br>
<a href="/r/DeepIntoYouTube" rel="nofollow">/r/DeepIntoYouTube</a><br>
<a href="/r/fifthworldproblems" rel="nofollow">/r/fifthworldproblems</a><br>
<a href="/r/awwwtf" rel="nofollow">/r/awwwtf</a><br>
<a href="/r/wellthatsucks" rel="nofollow">/r/wellthatsucks</a><br>
<a href="/r/streetfights" rel="nofollow">/r/streetfights</a><br>
<a href="/r/yesyesyesyesno" rel="nofollow">/r/yesyesyesyesno</a><br>
<a href="/r/wtfstockphotos" rel="nofollow">/r/wtfstockphotos</a><br>
<a href="/r/yesyesyesno" rel="nofollow">/r/yesyesyesno</a><br>
<a href="/r/maybemaybemaybe" rel="nofollow">/r/maybemaybemaybe</a><br>
<a href="/r/oddlyterrifying" rel="nofollow">/r/oddlyterrifying</a><br>
<a href="/r/thatlookedexpensive" rel="nofollow">/r/thatlookedexpensive</a><br>
<a href="/r/wtfgaragesale" rel="nofollow">/r/wtfgaragesale</a><br>
<a href="/r/Whatthefuckgetitoffme" rel="nofollow">/r/Whatthefuckgetitoffme</a> </p>
<h3 id="wiki_angering"><em>Angering</em></h3>
<p><a href="/r/mildlyinfuriating" rel="nofollow">/r/mildlyinfuriating</a><br>
<a href="/r/crappydesign" rel="nofollow">/r/crappydesign</a><br>
<a href="/r/rage" rel="nofollow">/r/rage</a><br>
<a href="/r/Bad_Cop_No_Donut" rel="nofollow">/r/Bad_Cop_No_Donut</a><br>
<a href="/r/gifsthatendtoosoon" rel="nofollow">/r/gifsthatendtoosoon</a><br>
<a href="/r/peoplebeingjerks" rel="nofollow">/r/peoplebeingjerks</a><br>
<a href="/r/casualchildabuse" rel="nofollow">/r/casualchildabuse</a><br>
<a href="/r/fuckthesepeople" rel="nofollow">/r/fuckthesepeople</a> </p>
<h3 id="wiki_edgy"><em>Edgy</em></h3>
<p><a href="/r/imgoingtohellforthis" rel="nofollow">/r/imgoingtohellforthis</a><br>
<a href="/r/toosoon" rel="nofollow">/r/toosoon</a> </p>
<h3 id="wiki_judgy"><em>Judgy</em></h3>
<p><a href="/r/trashy" rel="nofollow">/r/trashy</a><br>
<a href="/r/awfuleyebrows" rel="nofollow">/r/awfuleyebrows</a><br>
<a href="/r/awfuleverything" rel="nofollow">/r/awfuleverything</a><br>
<a href="/r/13or30" rel="nofollow">/r/13or30</a><br>
<a href="/r/ghettoglamourshots" rel="nofollow">/r/ghettoglamourshots</a><br>
<a href="/r/peopleofwalmart" rel="nofollow">/r/peopleofwalmart</a><br>
<a href="/r/hittablefaces" rel="nofollow">/r/hittablefaces</a><br>
<a href="/r/punchablefaces" rel="nofollow">/r/punchablefaces</a> </p>
<h3 id="wiki_scary_.28potentially_nsfl.29"><em>Scary (potentially NSFL)</em></h3>
<p><a href="/r/nosleep" rel="nofollow">/r/nosleep</a><br>
<a href="/r/morbidreality" rel="nofollow">/r/morbidreality</a><br>
<a href="/r/whatcouldgowrong" rel="nofollow">/r/whatcouldgowrong</a><br>
<a href="/r/Glitch_in_the_Matrix" rel="nofollow">/r/Glitch_in_the_Matrix</a><br>
<a href="/r/Paranormal" rel="nofollow">/r/Paranormal</a><br>
<a href="/r/nononono" rel="nofollow">/r/nononono</a><br>
<a href="/r/horror" rel="nofollow">/r/horror</a><br>
<a href="/r/shortscarystories" rel="nofollow">/r/shortscarystories</a><br>
<a href="/r/lastimages" rel="nofollow">/r/lastimages</a><br>
<a href="/r/peoplefuckingdying" rel="nofollow">/r/peoplefuckingdying</a><br>
<a href="/r/serialkillers" rel="nofollow">/r/serialkillers</a><br>
<a href="/r/WhyWereTheyFilming" rel="nofollow">/r/WhyWereTheyFilming</a><br>
<a href="/r/WinStupidPrizes" rel="nofollow">/r/WinStupidPrizes</a> </p>
<h4 id="wiki_creepy"><em>Creepy</em></h4>
<p><a href="/r/creepy" rel="nofollow">/r/creepy</a><br>
<a href="/r/creepypasta" rel="nofollow">/r/creepypasta</a><br>
<a href="/r/creepysigns" rel="nofollow">/r/creepysigns</a><br>
<a href="/r/megalophobia" rel="nofollow">/r/megalophobia</a> </p>
<h4 id="wiki_imaginary"><em>Imaginary</em></h4>
<p><a href="/r/ImaginaryMonsters" rel="nofollow">/r/ImaginaryMonsters</a><br>
<a href="/r/ImaginaryLeviathans" rel="nofollow">/r/ImaginaryLeviathans</a><br>
<a href="/r/ImaginaryMindscapes" rel="nofollow">/r/ImaginaryMindscapes</a><br>
<a href="/r/imaginarycharacters" rel="nofollow">/r/imaginarycharacters</a><br>
<a href="/r/imaginarylandscapes" rel="nofollow">/r/imaginarylandscapes</a><br>
<a href="/r/imaginarymaps" rel="nofollow">/r/imaginarymaps</a><br>
<a href="/r/SympatheticMonsters" rel="nofollow">/r/SympatheticMonsters</a> </p>
<h4 id="wiki_water_is_scary"><em>Water is scary</em></h4>
<p><a href="/r/thalassophobia" rel="nofollow">/r/thalassophobia</a><br>
<a href="/r/TheDepthsBelow" rel="nofollow">/r/TheDepthsBelow</a><br>
<a href="/r/submechanophobia" rel="nofollow">/r/submechanophobia</a> </p>
<h2 id="wiki_free_stuff"><strong>Free Stuff</strong></h2>
<p><a href="/r/freebies" rel="nofollow">/r/freebies</a><br>
<a href="/r/fullmoviesonyoutube" rel="nofollow">/r/fullmoviesonyoutube</a><br>
<a href="/r/efreebies" rel="nofollow">/r/efreebies</a><br>
<a href="/r/randomactsofgaming" rel="nofollow">/r/randomactsofgaming</a><br>
<a href="/r/freeEbooks" rel="nofollow">/r/freeEbooks</a><br>
<a href="/r/fullmoviesonvimeo" rel="nofollow">/r/fullmoviesonvimeo</a><br>
<a href="/r/freegamesonsteam" rel="nofollow">/r/freegamesonsteam</a><br>
<a href="/r/googleplaydeals" rel="nofollow">/r/googleplaydeals</a><br>
<a href="/r/megalinks" rel="nofollow">/r/megalinks</a><br>
<a href="/r/opendirectories" rel="nofollow">/r/opendirectories</a><br>
<a href="/r/Random_Acts_Of_Pizza" rel="nofollow">/r/Random_Acts_Of_Pizza</a><br>
<a href="/r/coupons" rel="nofollow">/r/coupons</a><br>
<a href="/r/dealsreddit" rel="nofollow">/r/dealsreddit</a><br>
<a href="/r/freegamefindings" rel="nofollow">/r/freegamefindings</a> </p>
<h2 id="wiki_gender2"><strong>Gender</strong></h2>
<h3 id="wiki_for_men"><strong>For Men</strong></h3>
<p><a href="/r/MaleFashionAdvice" rel="nofollow">/r/MaleFashionAdvice</a><br>
<a href="/r/everymanshouldknow" rel="nofollow">/r/everymanshouldknow</a><br>
<a href="/r/askmen" rel="nofollow">/r/askmen</a><br>
<a href="/r/frugalmalefashion" rel="nofollow">/r/frugalmalefashion</a><br>
<a href="/r/MensRights" rel="nofollow">/r/MensRights</a><br>
<a href="/r/malelifestyle" rel="nofollow">/r/malelifestyle</a><br>
<a href="/r/trollychromosome" rel="nofollow">/r/trollychromosome</a><br>
<a href="/r/malelivingspace" rel="nofollow">/r/malelivingspace</a><br>
<a href="/r/malehairadvice" rel="nofollow">/r/malehairadvice</a><br>
<a href="/r/malefashion" rel="nofollow">/r/malefashion</a><br>
<a href="/r/bigdickproblems" rel="nofollow">/r/bigdickproblems</a><br>
<a href="/r/mgtow" rel="nofollow">/r/mgtow</a> </p>
<h3 id="wiki_for_women"><strong>For Women</strong></h3>
<p><a href="/r/TwoXChromosomes" rel="nofollow">/r/TwoXChromosomes</a><br>
<a href="/r/askwomen" rel="nofollow">/r/askwomen</a><br>
<a href="/r/LadyBoners" rel="nofollow">/r/LadyBoners</a><br>
<a href="/r/TrollXChromosomes" rel="nofollow">/r/TrollXChromosomes</a><br>
<a href="/r/femalefashionadvice" rel="nofollow">/r/femalefashionadvice</a><br>
<a href="/r/xxfitness" rel="nofollow">/r/xxfitness</a><br>
<a href="/r/TheGirlSurvivalGuide" rel="nofollow">/r/TheGirlSurvivalGuide</a><br>
<a href="/r/abrathatfits" rel="nofollow">/r/abrathatfits</a><br>
<a href="/r/badwomensanatomy" rel="nofollow">/r/badwomensanatomy</a> </p>
<h2 id="wiki_geography"><strong>Geography</strong></h2>
<p><a href="http://www.reddit.com/r/LocationReddits/wiki/index" rel="nofollow">Looking for a subreddit for your area? Try looking here!</a> From <a href="/r/LocationReddits" rel="nofollow">/r/LocationReddits</a>.<br>
Note: Not all subreddits in that list are active.</p>
<p><a href="/r/MapPorn" rel="nofollow">/r/MapPorn</a><br>
<a href="/r/polandball" rel="nofollow">/r/polandball</a><br>
<a href="/r/vexillology" rel="nofollow">/r/vexillology</a> </p>
<h3 id="wiki_africa"><em>Africa</em></h3>
<p><a href="/r/SouthAfrica" rel="nofollow">/r/SouthAfrica</a> </p>
<h3 id="wiki_europe"><em>Europe</em></h3>
<p><a href="/r/europe" rel="nofollow">/r/europe</a><br>
<a href="/r/ireland" rel="nofollow">/r/ireland</a><br>
<a href="/r/thenetherlands" rel="nofollow">/r/thenetherlands</a><br>
<a href="/r/denmark" rel="nofollow">/r/denmark</a><br>
<a href="/r/italy" rel="nofollow">/r/italy</a><br>
<a href="/r/norge" rel="nofollow">/r/norge</a><br>
<a href="/r/polska" rel="nofollow">/r/polska</a><br>
<a href="/r/suomi" rel="nofollow">/r/suomi</a> (Finland)<br>
<a href="/r/romania" rel="nofollow">/r/romania</a><br>
<a href="/r/belgium" rel="nofollow">/r/belgium</a><br>
<a href="/r/scotland" rel="nofollow">/r/scotland</a><br>
<a href="/r/austria" rel="nofollow">/r/austria</a> </p>
<h4 id="wiki_france"><em>France</em></h4>
<p><a href="/r/france" rel="nofollow">/r/france</a><br>
<a href="/r/french" rel="nofollow">/r/french</a> </p>
<h4 id="wiki_germany"><em>Germany</em></h4>
<p><a href="/r/de" rel="nofollow">/r/de</a><br>
<a href="/r/germany" rel="nofollow">/r/germany</a><br>
<a href="/r/german" rel="nofollow">/r/german</a> </p>
<h4 id="wiki_russia"><em>Russia</em></h4>
<p><a href="/r/ANormalDayInRussia" rel="nofollow">/r/ANormalDayInRussia</a><br>
<a href="/r/youseecomrade" rel="nofollow">/r/youseecomrade</a> </p>
<h4 id="wiki_sweden"><em>Sweden</em></h4>
<p><a href="/r/sweden" rel="nofollow">/r/sweden</a><br>
<a href="/r/SWARJE" rel="nofollow">/r/SWARJE</a><br>
<a href="/r/swedishproblems" rel="nofollow">/r/swedishproblems</a><br>
<a href="/r/intresseklubben" rel="nofollow">/r/intresseklubben</a><br>
<a href="/r/svenskpolitik" rel="nofollow">/r/svenskpolitik</a><br>
<a href="/r/spop" rel="nofollow">/r/spop</a><br>
<a href="/r/Allsvenskan" rel="nofollow">/r/Allsvenskan</a> </p>
<h4 id="wiki_united_kingdom"><em>United Kingdom</em></h4>
<p><a href="/r/unitedkingdom" rel="nofollow">/r/unitedkingdom</a><br>
<a href="/r/britishproblems" rel="nofollow">/r/britishproblems</a><br>
<a href="/r/london" rel="nofollow">/r/london</a><br>
<a href="/r/ukpolitics" rel="nofollow">/r/ukpolitics</a><br>
<a href="/r/casualuk" rel="nofollow">/r/casualuk</a> </p>
<h3 id="wiki_north_america"><em>North America</em></h3>
<h4 id="wiki_canada"><em>Canada</em></h4>
<p><a href="/r/canada" rel="nofollow">/r/canada</a><br>
<a href="/r/toronto" rel="nofollow">/r/toronto</a><br>
<a href="/r/vancouver" rel="nofollow">/r/vancouver</a><br>
<a href="/r/canadapolitics" rel="nofollow">/r/canadapolitics</a><br>
<a href="/r/calgary" rel="nofollow">/r/calgary</a> </p>
<h4 id="wiki_mexico"><em>Mexico</em></h4>
<p><a href="/r/mexico" rel="nofollow">/r/mexico</a> </p>
<h4 id="wiki_usa.3A_united_states_of_america"><em>USA: United States of America</em></h4>
<p><a href="/r/MURICA" rel="nofollow">/r/MURICA</a><br>
<a href="/r/nyc" rel="nofollow">/r/nyc</a><br>
<a href="/r/chicago" rel="nofollow">/r/chicago</a><br>
<a href="/r/portland" rel="nofollow">/r/portland</a><br>
<a href="/r/boston" rel="nofollow">/r/boston</a><br>
<a href="/r/atlanta" rel="nofollow">/r/atlanta</a><br>
<a href="/r/washingtondc" rel="nofollow">/r/washingtondc</a><br>
<a href="/r/philadelphia" rel="nofollow">/r/philadelphia</a><br>
<a href="/r/newjersey" rel="nofollow">/r/newjersey</a><br>
<a href="/r/minnesota" rel="nofollow">/r/minnesota</a><br>
<a href="/r/michigan" rel="nofollow">/r/michigan</a> </p>
<h5 id="wiki_california"><em>California</em></h5>
<p><a href="/r/losangeles" rel="nofollow">/r/losangeles</a><br>
<a href="/r/sanfrancisco" rel="nofollow">/r/sanfrancisco</a><br>
<a href="/r/bayarea" rel="nofollow">/r/bayarea</a><br>
<a href="/r/california" rel="nofollow">/r/california</a><br>
<a href="/r/sandiego" rel="nofollow">/r/sandiego</a><br>
<a href="/r/disneyland" rel="nofollow">/r/disneyland</a> </p>
<h5 id="wiki_colorado"><em>Colorado</em></h5>
<p><a href="/r/denver" rel="nofollow">/r/denver</a><br>
<a href="/r/colorado" rel="nofollow">/r/colorado</a> </p>
<h5 id="wiki_florida"><em>Florida</em></h5>
<p><a href="/r/floridaman" rel="nofollow">/r/floridaman</a><br>
<a href="/r/waltdisneyworld" rel="nofollow">/r/waltdisneyworld</a> </p>
<h5 id="wiki_texas"><em>Texas</em></h5>
<p><a href="/r/austin" rel="nofollow">/r/austin</a><br>
<a href="/r/houston" rel="nofollow">/r/houston</a><br>
<a href="/r/texas" rel="nofollow">/r/texas</a><br>
<a href="/r/dallas" rel="nofollow">/r/dallas</a> </p>
<h5 id="wiki_washington"><em>Washington</em></h5>
<p><a href="/r/seattle" rel="nofollow">/r/seattle</a><br>
<a href="/r/SeattleWA" rel="nofollow">/r/SeattleWA</a> </p>
<h3 id="wiki_oceania"><em>Oceania</em></h3>
<p><a href="/r/australia" rel="nofollow">/r/australia</a><br>
<a href="/r/newzealand" rel="nofollow">/r/newzealand</a><br>
<a href="/r/melbourne" rel="nofollow">/r/melbourne</a><br>
<a href="/r/sydney" rel="nofollow">/r/sydney</a> </p>
<h3 id="wiki_asia"><em>Asia</em></h3>
<p><a href="/r/Philippines" rel="nofollow">/r/Philippines</a><br>
<a href="/r/india" rel="nofollow">/r/india</a><br>
<a href="/r/singapore" rel="nofollow">/r/singapore</a><br>
<a href="/r/china" rel="nofollow">/r/china</a><br>
<a href="/r/hongkong" rel="nofollow">/r/hongkong</a> </p>
<h4 id="wiki_japan"><em>Japan</em></h4>
<p><a href="/r/japan" rel="nofollow">/r/japan</a><br>
<a href="/r/japanpics" rel="nofollow">/r/japanpics</a><br>
<a href="/r/japantravel" rel="nofollow">/r/japantravel</a> </p>
<h4 id="wiki_korea"><em>Korea</em></h4>
<p><a href="/r/kpop" rel="nofollow">/r/kpop</a><br>
<a href="/r/pyongyang" rel="nofollow">/r/pyongyang</a><br>
<a href="/r/korea" rel="nofollow">/r/korea</a> </p>
<h3 id="wiki_south_america"><em>South America</em></h3>
<p><a href="/r/brasil" rel="nofollow">/r/brasil</a><br>
<a href="/r/argentina" rel="nofollow">/r/argentina</a> </p>
<h2 id="wiki_meta"><strong>Meta</strong></h2>
<p><a href="/r/OutOfTheLoop" rel="nofollow">/r/OutOfTheLoop</a><br>
<a href="/r/nocontext" rel="nofollow">/r/nocontext</a><br>
<a href="/r/tldr" rel="nofollow">/r/tldr</a><br>
<a href="/r/modnews" rel="nofollow">/r/modnews</a><br>
<a href="/r/Enhancement" rel="nofollow">/r/Enhancement</a><br>
<a href="/r/SecretSanta" rel="nofollow">/r/SecretSanta</a><br>
<a href="/r/MuseumOfReddit" rel="nofollow">/r/MuseumOfReddit</a><br>
<a href="/r/theoryofreddit" rel="nofollow">/r/theoryofreddit</a><br>
<a href="/r/threadkillers" rel="nofollow">/r/threadkillers</a><br>
<a href="/r/evenwithcontext" rel="nofollow">/r/evenwithcontext</a><br>
<a href="/r/beetlejuicing" rel="nofollow">/r/beetlejuicing</a><br>
<a href="/r/againsthatesubreddits" rel="nofollow">/r/againsthatesubreddits</a><br>
<a href="/r/redditinreddit" rel="nofollow">/r/redditinreddit</a> </p>
<h3 id="wiki_administrative"><strong>Administrative</strong></h3>
<p><a href="/r/announcements" rel="nofollow">/r/announcements</a><br>
<a href="/r/blog" rel="nofollow">/r/blog</a><br>
<a href="/r/beta" rel="nofollow">/r/beta</a> </p>
<h3 id="wiki_apps"><em>Apps</em></h3>
<p><a href="/r/baconreader" rel="nofollow">/r/baconreader</a><br>
<a href="/r/alienblue" rel="nofollow">/r/alienblue</a><br>
<a href="/r/baconit" rel="nofollow">/r/baconit</a><br>
<a href="/r/redditsync" rel="nofollow">/r/redditsync</a><br>
<a href="/r/relayforreddit" rel="nofollow">/r/relayforreddit</a><br>
<a href="/r/apolloapp" rel="nofollow">/r/apolloapp</a><br>
<a href="/r/redditmobile" rel="nofollow">/r/redditmobile</a> </p>
<h3 id="wiki_circlejerks"><em>Circlejerks</em></h3>
<p><a href="/r/Circlejerk" rel="nofollow">/r/Circlejerk</a><br>
<a href="/r/DiWHY" rel="nofollow">/r/DiWHY</a><br>
<a href="/r/frugal_jerk" rel="nofollow">/r/frugal_jerk</a> </p>
<h3 id="wiki_drama"><em>Drama</em></h3>
<p><a href="/r/SubredditDrama" rel="nofollow">/r/SubredditDrama</a><br>
<a href="/r/drama" rel="nofollow">/r/drama</a><br>
<a href="/r/hobbydrama" rel="nofollow">/r/hobbydrama</a> </p>
<h3 id="wiki_negative"><em>Negative</em></h3>
<p><a href="/r/ShitRedditSays" rel="nofollow">/r/ShitRedditSays</a><br>
<a href="/r/karmaconspiracy" rel="nofollow">/r/karmaconspiracy</a><br>
<a href="/r/undelete" rel="nofollow">/r/undelete</a><br>
<a href="/r/jesuschristreddit" rel="nofollow">/r/jesuschristreddit</a><br>
<a href="/r/karmacourt" rel="nofollow">/r/karmacourt</a><br>
<a href="/r/titlegore" rel="nofollow">/r/titlegore</a><br>
<a href="/r/ShitAmericansSay" rel="nofollow">/r/ShitAmericansSay</a> </p>
<h3 id="wiki_positive"><em>Positive</em></h3>
<p><strong><a href="/r/bestof" rel="nofollow">/r/bestof</a></strong><br>
<a href="/r/DepthHub" rel="nofollow">/r/DepthHub</a><br>
<a href="/r/BestOfReports" rel="nofollow">/r/BestOfReports</a><br>
<a href="/r/bestoflegaladvice" rel="nofollow">/r/bestoflegaladvice</a> </p>
<h3 id="wiki_subreddits"><em>Subreddits</em></h3>
<p><a href="/r/subredditoftheday" rel="nofollow">/r/subredditoftheday</a><br>
<a href="/r/wowthissubexists" rel="nofollow">/r/wowthissubexists</a><br>
<a href="/r/newreddits" rel="nofollow">/r/newreddits</a><br>
<a href="/r/ofcoursethatsathing" rel="nofollow">/r/ofcoursethatsathing</a><br>
<a href="/r/findareddit" rel="nofollow">/r/findareddit</a> </p>
<h4 id="wiki_subreddit_simulator"><em>Subreddit Simulator</em></h4>
<p><a href="/r/subredditsimulator" rel="nofollow">/r/subredditsimulator</a><br>
<a href="/r/subredditsimmeta" rel="nofollow">/r/subredditsimmeta</a> </p>
<h2 id="wiki_general6"><strong>General</strong></h2>
<p><a href="/r/TrueReddit" rel="nofollow">/r/TrueReddit</a><br>
<a href="/r/awesome" rel="nofollow">/r/awesome</a> </p>
<h3 id="wiki_looking_for_something"><em>Looking for something</em></h3>
<p><a href="/r/TipOfMyTongue" rel="nofollow">/r/TipOfMyTongue</a><br>
<a href="/r/TipOfMyPenis" rel="nofollow">/r/TipOfMyPenis</a> (NSFW)     </p>
<h2 id="wiki_mind_blowing"><strong>Mind blowing</strong></h2>
<p><a href="/r/woahdude" rel="nofollow">/r/woahdude</a><br>
<a href="/r/frisson" rel="nofollow">/r/frisson</a><br>
<a href="/r/asmr" rel="nofollow">/r/asmr</a><br>
<a href="/r/VaporwaveAesthetics" rel="nofollow">/r/VaporwaveAesthetics</a><br>
<a href="/r/glitchinthematrix" rel="nofollow">/r/glitchinthematrix</a> </p>
<h2 id="wiki_nature2"><strong>Nature</strong></h2>
<p><a href="/r/earthporn" rel="nofollow">/r/earthporn</a><br>
<a href="/r/hardcoreaww" rel="nofollow">/r/hardcoreaww</a><br>
<a href="/r/hitmanimals" rel="nofollow">/r/hitmanimals</a><br>
<a href="/r/natureisfuckinglit" rel="nofollow">/r/natureisfuckinglit</a><br>
<a href="/r/heavyseas" rel="nofollow">/r/heavyseas</a> </p>
<h3 id="wiki_plants.2Ffungi"><em>Plants/Fungi</em></h3>
<p><a href="/r/marijuanaenthusiasts" rel="nofollow">/r/marijuanaenthusiasts</a><br>
<a href="/r/succulents" rel="nofollow">/r/succulents</a><br>
<a href="/r/mycology" rel="nofollow">/r/mycology</a><br>
<a href="/r/bonsai" rel="nofollow">/r/bonsai</a><br>
<a href="/r/TreesSuckingOnThings" rel="nofollow">/r/TreesSuckingOnThings</a> </p>
<h3 id="wiki_violent_nature"><em>Violent Nature</em></h3>
<p><a href="/r/natureismetal" rel="nofollow">/r/natureismetal</a><br>
<a href="/r/Natureisbrutal" rel="nofollow">/r/Natureisbrutal</a><br>
<a href="/r/naturewasmetal" rel="nofollow">/r/naturewasmetal</a> </p>
<h3 id="wiki_weather"><em>Weather</em></h3>
<p><a href="/r/weathergifs" rel="nofollow">/r/weathergifs</a><br>
<a href="/r/tropicalweather" rel="nofollow">/r/tropicalweather</a> </p>
<h2 id="wiki_news.2Fpolitics"><strong>News/Politics</strong></h2>
<h3 id="wiki_news"><em>News</em></h3>
<p><a href="/r/worldnews" rel="nofollow">/r/worldnews</a><br>
<a href="/r/news" rel="nofollow">/r/news</a><br>
<a href="/r/nottheonion" rel="nofollow">/r/nottheonion</a><br>
<a href="/r/UpliftingNews" rel="nofollow">/r/UpliftingNews</a><br>
<a href="/r/offbeat" rel="nofollow">/r/offbeat</a><br>
<a href="/r/gamernews" rel="nofollow">/r/gamernews</a><br>
<a href="/r/floridaman" rel="nofollow">/r/floridaman</a><br>
<a href="/r/energy" rel="nofollow">/r/energy</a><br>
<a href="/r/syriancivilwar" rel="nofollow">/r/syriancivilwar</a><br>
<a href="/r/truecrime" rel="nofollow">/r/truecrime</a> </p>
<h4 id="wiki_fake_news"><em>Fake News</em></h4>
<p><a href="/r/TheOnion" rel="nofollow">/r/TheOnion</a><br>
<a href="/r/AteTheOnion" rel="nofollow">/r/AteTheOnion</a> </p>
<h3 id="wiki_politics"><em>Politics</em></h3>
<p>For more, see <a href="http://www.reddit.com/r/politics/wiki/relatedsubs" rel="nofollow">the list compiled in the wiki</a> of <a href="/r/Politics" rel="nofollow">/r/Politics</a>!<br>
Note: Not all subreddits in that list are active.</p>
<p><a href="/r/Politics" rel="nofollow">/r/Politics</a><br>
<a href="/r/worldpolitics" rel="nofollow">/r/worldpolitics</a><br>
<a href="/r/Libertarian" rel="nofollow">/r/Libertarian</a><br>
<a href="/r/anarchism" rel="nofollow">/r/anarchism</a><br>
<a href="/r/socialism" rel="nofollow">/r/socialism</a><br>
<a href="/r/conservative" rel="nofollow">/r/conservative</a><br>
<a href="/r/politicalhumor" rel="nofollow">/r/politicalhumor</a><br>
<a href="/r/neutralpolitics" rel="nofollow">/r/neutralpolitics</a><br>
<a href="/r/politicaldiscussion" rel="nofollow">/r/politicaldiscussion</a><br>
<a href="/r/ukpolitics" rel="nofollow">/r/ukpolitics</a><br>
<a href="/r/geopolitics" rel="nofollow">/r/geopolitics</a><br>
<a href="/r/communism" rel="nofollow">/r/communism</a><br>
<a href="/r/completeanarchy" rel="nofollow">/r/completeanarchy</a> </p>
<h4 id="wiki_alt-right"><em>Alt-Right</em></h4>
<p><a href="/r/the_donald" rel="nofollow">/r/the_donald</a><br>
<a href="/r/HillaryForPrison" rel="nofollow">/r/HillaryForPrison</a><br>
<a href="/r/wikileaks" rel="nofollow">/r/wikileaks</a> </p>
<h4 id="wiki_capitalism"><em>Capitalism</em></h4>
<p><a href="/r/latestagecapitalism" rel="nofollow">/r/latestagecapitalism</a><br>
<a href="/r/anarcho_capitalism" rel="nofollow">/r/anarcho_capitalism</a> </p>
<h4 id="wiki_gender_politics"><em>Gender Politics</em></h4>
<p><a href="/r/MensRights" rel="nofollow">/r/MensRights</a><br>
<a href="/r/feminism" rel="nofollow">/r/feminism</a> </p>
<h4 id="wiki_left"><em>Left</em></h4>
<p><a href="/r/SandersForPresident" rel="nofollow">/r/SandersForPresident</a><br>
<a href="/r/bidenbro" rel="nofollow">/r/bidenbro</a><br>
<a href="/r/political_revolution" rel="nofollow">/r/political_revolution</a><br>
<a href="/r/thanksobama" rel="nofollow">/r/thanksobama</a><br>
<a href="/r/esist" rel="nofollow">/r/esist</a><br>
<a href="/r/The_Mueller" rel="nofollow">/r/The_Mueller</a><br>
<a href="/r/bluemidterm2018" rel="nofollow">/r/bluemidterm2018</a><br>
<a href="/r/fuckthealtright" rel="nofollow">/r/fuckthealtright</a><br>
<a href="/r/democrats" rel="nofollow">/r/democrats</a><br>
<a href="/r/liberal" rel="nofollow">/r/liberal</a><br>
<a href="/r/keep_track" rel="nofollow">/r/keep_track</a> </p>
<h5 id="wiki_anti-trump"><em>Anti-Trump</em></h5>
<p><a href="/r/enoughtrumpspam" rel="nofollow">/r/enoughtrumpspam</a><br>
<a href="/r/MarchAgainstTrump" rel="nofollow">/r/MarchAgainstTrump</a><br>
<a href="/r/TinyTrumps" rel="nofollow">/r/TinyTrumps</a><br>
<a href="/r/TrumpCriticizesTrump" rel="nofollow">/r/TrumpCriticizesTrump</a><br>
<a href="/r/trumpgret" rel="nofollow">/r/trumpgret</a><br>
<a href="/r/impeach_trump" rel="nofollow">/r/impeach_trump</a> </p>
<h2 id="wiki_nostalgia.2Ftime"><strong>Nostalgia/Time</strong></h2>
<p><a href="/r/OldSchoolCool" rel="nofollow">/r/OldSchoolCool</a><br>
<a href="/r/TheWayWeWere" rel="nofollow">/r/TheWayWeWere</a><br>
<a href="/r/nostalgia" rel="nofollow">/r/nostalgia</a><br>
<a href="/r/vinyl" rel="nofollow">/r/vinyl</a><br>
<a href="/r/forwardsfromgrandma" rel="nofollow">/r/forwardsfromgrandma</a><br>
<a href="/r/oldphotosinreallife" rel="nofollow">/r/oldphotosinreallife</a> </p>
<h2 id="wiki_parodies"><strong>Parodies</strong></h2>
<p><a href="/r/firstworldanarchists" rel="nofollow">/r/firstworldanarchists</a><br>
<a href="/r/wheredidthesodago" rel="nofollow">/r/wheredidthesodago</a><br>
<a href="/r/unexpectedthuglife" rel="nofollow">/r/unexpectedthuglife</a><br>
<a href="/r/youdontsurf" rel="nofollow">/r/youdontsurf</a><br>
<a href="/r/montageparodies" rel="nofollow">/r/montageparodies</a><br>
<a href="/r/outside" rel="nofollow">/r/outside</a><br>
<a href="/r/OSHA" rel="nofollow">/r/OSHA</a><br>
<a href="/r/hailcorporate" rel="nofollow">/r/hailcorporate</a><br>
<a href="/r/im14andthisisdeep" rel="nofollow">/r/im14andthisisdeep</a><br>
<a href="/r/bollywoodrealism" rel="nofollow">/r/bollywoodrealism</a><br>
<a href="/r/AccidentalRenaissance" rel="nofollow">/r/AccidentalRenaissance</a><br>
<a href="/r/maliciouscompliance" rel="nofollow">/r/maliciouscompliance</a><br>
<a href="/r/fakehistoryporn" rel="nofollow">/r/fakehistoryporn</a><br>
<a href="/r/coaxedintoasnafu" rel="nofollow">/r/coaxedintoasnafu</a><br>
<a href="/r/irleastereggs" rel="nofollow">/r/irleastereggs</a> </p>
<h2 id="wiki_sfwporn_network"><strong>SFWPorn Network</strong></h2>
<p><a href="http://www.reddit.com/r/ListOfSubreddits/wiki/sfwpornnetwork" rel="nofollow">SFWPorn Network wiki</a> from <a href="http://www.reddit.com/user/kjoneslol/m/sfwpornnetwork" rel="nofollow">multi</a> by <a href="/u/kjoneslol" rel="nofollow">/u/kjoneslol</a>.<br>
<a href="http://www.reddit.com/r/sfwpornnetwork/wiki/network#wiki_nature" rel="nofollow">See more here!</a> Via <a href="/r/sfwpornnetwork" rel="nofollow">/r/sfwpornnetwork</a>.  </p>
<p><a href="/r/EarthPorn" rel="nofollow">/r/EarthPorn</a><br>
<a href="/r/HistoryPorn" rel="nofollow">/r/HistoryPorn</a><br>
<a href="/r/FoodPorn" rel="nofollow">/r/FoodPorn</a><br>
<a href="/r/JusticePorn" rel="nofollow">/r/JusticePorn</a><br>
<a href="/r/AbandonedPorn" rel="nofollow">/r/AbandonedPorn</a><br>
<a href="/r/SpacePorn" rel="nofollow">/r/SpacePorn</a><br>
<a href="/r/RoomPorn" rel="nofollow">/r/RoomPorn</a><br>
<a href="/r/QuotesPorn" rel="nofollow">/r/QuotesPorn</a><br>
<a href="/r/MapPorn" rel="nofollow">/r/MapPorn</a><br>
<a href="/r/CityPorn" rel="nofollow">/r/CityPorn</a><br>
<a href="/r/carporn" rel="nofollow">/r/carporn</a><br>
<a href="/r/humanporn" rel="nofollow">/r/humanporn</a><br>
<a href="/r/penmanshipporn" rel="nofollow">/r/penmanshipporn</a><br>
<a href="/r/militaryporn" rel="nofollow">/r/militaryporn</a><br>
<a href="/r/DesignPorn" rel="nofollow">/r/DesignPorn</a><br>
<a href="/r/ThingsCutInHalfPorn" rel="nofollow">/r/ThingsCutInHalfPorn</a><br>
<a href="/r/ArchitecturePorn" rel="nofollow">/r/ArchitecturePorn</a><br>
<a href="/r/ExposurePorn" rel="nofollow">/r/ExposurePorn</a><br>
<a href="/r/futureporn" rel="nofollow">/r/futureporn</a><br>
<a href="/r/adrenalineporn" rel="nofollow">/r/adrenalineporn</a><br>
<a href="/r/waterporn" rel="nofollow">/r/waterporn</a><br>
<a href="/r/machineporn" rel="nofollow">/r/machineporn</a><br>
<a href="/r/animalporn" rel="nofollow">/r/animalporn</a><br>
<a href="/r/movieposterporn" rel="nofollow">/r/movieposterporn</a><br>
<a href="/r/illusionporn" rel="nofollow">/r/illusionporn</a><br>
<a href="/r/destructionporn" rel="nofollow">/r/destructionporn</a><br>
<a href="/r/adporn" rel="nofollow">/r/adporn</a><br>
<a href="/r/artefactporn" rel="nofollow">/r/artefactporn</a><br>
<a href="/r/gunporn" rel="nofollow">/r/gunporn</a><br>
<a href="/r/skyporn" rel="nofollow">/r/skyporn</a><br>
<a href="/r/powerwashingporn" rel="nofollow">/r/powerwashingporn</a><br>
<a href="/r/ArtPorn" rel="nofollow">/r/ArtPorn</a><br>
<a href="/r/InfrastructurePorn" rel="nofollow">/r/InfrastructurePorn</a><br>
<a href="/r/VillagePorn" rel="nofollow">/r/VillagePorn</a><br>
<a href="/r/shockwaveporn" rel="nofollow">/r/shockwaveporn</a><br>
<a href="/r/productporn" rel="nofollow">/r/productporn</a><br>
<a href="/r/macroporn" rel="nofollow">/r/macroporn</a><br>
<a href="/r/cabinporn" rel="nofollow">/r/cabinporn</a><br>
<a href="/r/houseporn" rel="nofollow">/r/houseporn</a><br>
<a href="/r/mineralporn" rel="nofollow">/r/mineralporn</a><br>
<a href="/r/microporn" rel="nofollow">/r/microporn</a> </p>
<h2 id="wiki_shitty"><strong>Shitty</strong></h2>
<p><a href="/r/shittyaskscience" rel="nofollow">/r/shittyaskscience</a><br>
<a href="/r/shittyfoodporn" rel="nofollow">/r/shittyfoodporn</a><br>
<a href="/r/shittyreactiongifs" rel="nofollow">/r/shittyreactiongifs</a><br>
<a href="/r/crappydesign" rel="nofollow">/r/crappydesign</a><br>
<a href="/r/Shitty_Car_Mods" rel="nofollow">/r/Shitty_Car_Mods</a><br>
<a href="/r/shittyadvice" rel="nofollow">/r/shittyadvice</a><br>
<a href="/r/shittyrobots" rel="nofollow">/r/shittyrobots</a><br>
<a href="/r/ShittyLifeProTips" rel="nofollow">/r/ShittyLifeProTips</a><br>
<a href="/r/shittykickstarters" rel="nofollow">/r/shittykickstarters</a><br>
<a href="/r/shittyanimalfacts" rel="nofollow">/r/shittyanimalfacts</a><br>
<a href="/r/shitpost" rel="nofollow">/r/shitpost</a><br>
<a href="/r/shittymoviedetails" rel="nofollow">/r/shittymoviedetails</a> </p>
<h2 id="wiki_unexpected"><strong>Unexpected</strong></h2>
<p><a href="/r/unexpected" rel="nofollow">/r/unexpected</a><br>
<a href="/r/UnexpectedThugLife" rel="nofollow">/r/UnexpectedThugLife</a><br>
<a href="/r/misleadingthumbnails" rel="nofollow">/r/misleadingthumbnails</a><br>
<a href="/r/unexpectedjihad" rel="nofollow">/r/unexpectedjihad</a><br>
<a href="/r/slygifs" rel="nofollow">/r/slygifs</a><br>
<a href="/r/blackmagicfuckery" rel="nofollow">/r/blackmagicfuckery</a><br>
<a href="/r/unexpectedhogwarts" rel="nofollow">/r/unexpectedhogwarts</a><br>
<a href="/r/UnexpectedMulaney" rel="nofollow">/r/UnexpectedMulaney</a> </p>
<h2 id="wiki_visually_appealing"><strong>Visually Appealing</strong></h2>
<p><a href="/r/AbandonedPorn" rel="nofollow">/r/AbandonedPorn</a><br>
<a href="/r/OddlySatisfying" rel="nofollow">/r/OddlySatisfying</a><br>
<a href="/r/RoomPorn" rel="nofollow">/r/RoomPorn</a><br>
<a href="/r/nonononoyes" rel="nofollow">/r/nonononoyes</a><br>
<a href="/r/minimalism" rel="nofollow">/r/minimalism</a><br>
<a href="/r/CityPorn" rel="nofollow">/r/CityPorn</a><br>
<a href="/r/penmanshipporn" rel="nofollow">/r/penmanshipporn</a><br>
<a href="/r/Cinemagraphs" rel="nofollow">/r/Cinemagraphs</a><br>
<a href="/r/ImaginaryLandscapes" rel="nofollow">/r/ImaginaryLandscapes</a><br>
<a href="/r/eyebleach" rel="nofollow">/r/eyebleach</a><br>
<a href="/r/DesignPorn" rel="nofollow">/r/DesignPorn</a><br>
<a href="/r/perfectloops" rel="nofollow">/r/perfectloops</a><br>
<a href="/r/perfectfit" rel="nofollow">/r/perfectfit</a><br>
<a href="/r/humansbeingbros" rel="nofollow">/r/humansbeingbros</a><br>
<a href="/r/powerwashingporn" rel="nofollow">/r/powerwashingporn</a><br>
<a href="/r/nevertellmetheodds" rel="nofollow">/r/nevertellmetheodds</a><br>
<a href="/r/typography" rel="nofollow">/r/typography</a><br>
<a href="/r/cozyplaces" rel="nofollow">/r/cozyplaces</a><br>
<a href="/r/breathinginformation" rel="nofollow">/r/breathinginformation</a><br>
<a href="/r/desirepath" rel="nofollow">/r/desirepath</a><br>
<a href="/r/tiltshift" rel="nofollow">/r/tiltshift</a><br>
<a href="/r/mostbeautiful" rel="nofollow">/r/mostbeautiful</a><br>
<a href="/r/AmateurRoomPorn" rel="nofollow">/r/AmateurRoomPorn</a><br>
<a href="/r/slygifs" rel="nofollow">/r/slygifs</a><br>
<a href="/r/raining" rel="nofollow">/r/raining</a><br>
<a href="/r/AccidentalWesAnderson" rel="nofollow">/r/AccidentalWesAnderson</a><br>
<a href="/r/unstirredpaint" rel="nofollow">/r/unstirredpaint</a><br>
<a href="/r/handwriting" rel="nofollow">/r/handwriting</a><br>
<a href="/r/thatpeelingfeeling" rel="nofollow">/r/thatpeelingfeeling</a> </p>

<h2 id="wiki_hold_my_____"><em>Hold My ____</em></h2>
<p><a href="/r/holdmybeer" rel="nofollow">/r/holdmybeer</a><br>
<a href="/r/holdmyjuicebox" rel="nofollow">/r/holdmyjuicebox</a><br>
<a href="/r/holdmyfries" rel="nofollow">/r/holdmyfries</a><br>
<a href="/r/holdmybeaker" rel="nofollow">/r/holdmybeaker</a><br>
<a href="/r/holdmycosmo" rel="nofollow">/r/holdmycosmo</a><br>
<a href="/r/holdmycatnip" rel="nofollow">/r/holdmycatnip</a><br>
<a href="/r/holdmyredbull" rel="nofollow">/r/holdmyredbull</a><br>
<a href="/r/holdmyfeedingtube" rel="nofollow">/r/holdmyfeedingtube</a> </p>

<h2 id="wiki_weird_feelings.2Fcategorize_later"><strong>Weird Feelings/Categorize Later</strong></h2>
<p><a href="/r/fiftyfifty" rel="nofollow">/r/fiftyfifty</a><br>
<a href="/r/firstworldproblems" rel="nofollow">/r/firstworldproblems</a><br>
<a href="/r/idiotsfightingthings" rel="nofollow">/r/idiotsfightingthings</a><br>
<a href="/r/whatsinthisthing" rel="nofollow">/r/whatsinthisthing</a>   see also: <a href="http://www.reddit.com/user/AskReddit_Multis/m/what_is_this___" rel="nofollow">related subreddits</a> from <a href="/r/AskReddit" rel="nofollow">/r/AskReddit</a><br>
<a href="/r/notinteresting" rel="nofollow">/r/notinteresting</a><br>
<a href="/r/fifthworldpics" rel="nofollow">/r/fifthworldpics</a><br>
<a href="/r/drunkorakid" rel="nofollow">/r/drunkorakid</a><br>
<a href="/r/pussypassdenied" rel="nofollow">/r/pussypassdenied</a><br>
<a href="/r/UNBGBBIIVCHIDCTIICBG" rel="nofollow">/r/UNBGBBIIVCHIDCTIICBG</a><br>
<a href="/r/Justfuckmyshitup" rel="nofollow">/r/Justfuckmyshitup</a><br>
<a href="/r/BestOfStreamingVideo" rel="nofollow">/r/BestOfStreamingVideo</a><br>
<a href="/r/CatastrophicFailure" rel="nofollow">/r/CatastrophicFailure</a><br>
<a href="/r/evilbuildings" rel="nofollow">/r/evilbuildings</a><br>
<a href="/r/urbanhell" rel="nofollow">/r/urbanhell</a><br>
<a href="/r/justiceserved" rel="nofollow">/r/justiceserved</a><br>
<a href="/r/mypeopleneedme" rel="nofollow">/r/mypeopleneedme</a><br>
<a href="/r/notmyjob" rel="nofollow">/r/notmyjob</a><br>
<a href="/r/onejob" rel="nofollow">/r/onejob</a><br>
<a href="/r/sweatypalms" rel="nofollow">/r/sweatypalms</a><br>
<a href="/r/therewasanattempt" rel="nofollow">/r/therewasanattempt</a><br>
<a href="/r/bitchimabus" rel="nofollow">/r/bitchimabus</a><br>
<a href="/r/greendawn" rel="nofollow">/r/greendawn</a><br>
<a href="/r/thingsforants" rel="nofollow">/r/thingsforants</a><br>
<a href="/r/youseeingthisshit" rel="nofollow">/r/youseeingthisshit</a><br>
<a href="/r/hmmm" rel="nofollow">/r/hmmm</a><br>
<a href="/r/hadtohurt" rel="nofollow">/r/hadtohurt</a><br>
<a href="/r/MandelaEffect" rel="nofollow">/r/MandelaEffect</a><br>
<a href="/r/mildlypenis" rel="nofollow">/r/mildlypenis</a><br>
<a href="/r/redditdayof" rel="nofollow">/r/redditdayof</a><br>
<a href="/r/idiotsincars" rel="nofollow">/r/idiotsincars</a><br>
<a href="/r/instantkarma" rel="nofollow">/r/instantkarma</a><br>
<a href="/r/2healthbars" rel="nofollow">/r/2healthbars</a><br>
<a href="/r/collapse" rel="nofollow">/r/collapse</a><br>
<a href="/r/slavs_squatting" rel="nofollow">/r/slavs_squatting</a><br>
<a href="/r/confusing_perspective" rel="nofollow">/r/confusing_perspective</a><br>
<a href="/r/the_pack" rel="nofollow">/r/the_pack</a><br>
<a href="/r/unpopularopinion" rel="nofollow">/r/unpopularopinion</a><br>
<a href="/r/okbuddyretard" rel="nofollow">/r/okbuddyretard</a><br>
<a href="/r/nextfuckinglevel" rel="nofollow">/r/nextfuckinglevel</a><br>
<a href="/r/ooer" rel="nofollow">/r/ooer</a><br>
<a href="/r/happycryingdads" rel="nofollow">/r/happycryingdads</a><br>
<a href="/r/dashcamgifs" rel="nofollow">/r/dashcamgifs</a><br>
<a href="/r/FullScorpion" rel="nofollow">/r/FullScorpion</a><br>
<a href="/r/instantregret" rel="nofollow">/r/instantregret</a><br>
<a href="/r/MildlyVandalised" rel="nofollow">/r/MildlyVandalised</a><br>
<a href="/r/watchpeoplesurvive" rel="nofollow">/r/watchpeoplesurvive</a><br>
<a href="/r/tendies" rel="nofollow">/r/tendies</a><br>
<a href="/r/dontputyourdickinthat" rel="nofollow">/r/dontputyourdickinthat</a><br>
<a href="/r/whatintarnation" rel="nofollow">/r/whatintarnation</a><br>
<a href="/r/tworedditorsonecup" rel="nofollow">/r/tworedditorsonecup</a><br>
<a href="/r/ExpandDong" rel="nofollow">/r/ExpandDong</a><br>
<a href="/r/wackytictacs" rel="nofollow">/r/wackytictacs</a><br>
<a href="/r/halloween" rel="nofollow">/r/halloween</a><br>
<a href="/r/whatcouldgoright" rel="nofollow">/r/whatcouldgoright</a><br>
<a href="/r/hmmmgifs" rel="nofollow">/r/hmmmgifs</a><br>
<a href="/r/bizarrebuildings" rel="nofollow">/r/bizarrebuildings</a><br>
<a href="/r/inclusiveor" rel="nofollow">/r/inclusiveor</a><br>
<a href="/r/lostgeneration" rel="nofollow">/r/lostgeneration</a><br>
<a href="/r/kurzgesagt" rel="nofollow">/r/kurzgesagt</a><br>
<a href="/r/boop" rel="nofollow">/r/boop</a> </p>

<h1 id="wiki_ex_50k.2B">Ex 50k+</h1>
<p><a href="/r/mindcrack" rel="nofollow">/r/mindcrack</a><br>
<a href="/r/twitchplayspokemon" rel="nofollow">/r/twitchplayspokemon</a><br>
<a href="/r/battlefield3" rel="nofollow">/r/battlefield3</a><br>
<a href="/r/punchablefaces" rel="nofollow">/r/punchablefaces</a><br>
<a href="/r/csgobetting" rel="nofollow">/r/csgobetting</a><br>
<a href="/r/historicalwhatif" rel="nofollow">/r/historicalwhatif</a> </p>
"""
soup = BeautifulSoup(txt,"html.parser")
db_dict = []
for i in soup.find_all('h1'):
    db_dict.append(i.text)

db_list = {}
category = ''
subreddits = []
for i in soup.text.split('\n'):
    if i.find('more') == -1 and i.find('Note') == -1 and len(i.split(' ')) < 6:
        if i[:3] != "/r/" and i not in db_dict:
            db_list[category] = subreddits[:]
            subreddits.clear()
            category = i
        elif i[:3] == "/r/":
            subreddits.append(i.split(" ")[0])

db_list = {key:val for key, val in db_list.items() if val != []}

obj = store_data()
csr = obj.connect_db('reddit_database.db')
for cat in db_list:
    print(cat)
    for subr in db_list[cat]:
        print("------{}----".format(subr))
        obj.subreddit_table(csr=csr, name=cat, subreddit=str(subr),date=str(datetime.datetime.now()))




