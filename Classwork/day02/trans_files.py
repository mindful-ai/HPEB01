Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\B01\day02\hotel_california.txt", "r")
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\Clients\\HPE\\B01\\day02\\hotel_california.txt' mode='r' encoding='cp1252'>
>>> path = "c:\new\temp\random\example.txt"
>>> print(path)
c:
ew	empandom\example.txt
>>> path = r"c:\new\temp\random\example.txt"
>>> print(path)
c:\new\temp\random\example.txt
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\Clients\\HPE\\B01\\day02\\hotel_california.txt' mode='r' encoding='cp1252'>
>>> content = f.read()
>>> content
'On a dark desert highway, cool wind in my hair\nWarm smell of colitas, rising up through the air\nUp ahead in the distance, I saw a shimmering light\nMy head grew heavy and my sight grew dim\nI had to stop for the night.\nThere she stood in the doorway;\nI heard the mission bell\nAnd I was thinking to myself\n\'This could be heaven or this could be Hell\'\nThen she lit up a candle and she showed me the way\nThere were voices down the corridor,\nI thought I heard them say\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face.\nPlenty of room at the Hotel California\nAny time of year (any time of year) you can find it here\nHer mind is Tiffany-twisted, she got the Mercedes bends\nShe got a lot of pretty, pretty boys, that she calls friends\nHow they dance in the courtyard, sweet summer sweat\nSome dance to remember, some dance to forget\nSo I called up the Captain,\n\'Please bring me my wine\'\nHe said, \'we haven\'t had that spirit here since nineteen sixty-nine\'\nAnd still those voices are calling from far away,\nWake you up in the middle of the night\nJust to hear them say"\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face.\nThey livin\' it up at the Hotel California\nWhat a nice surprise (what a nice surprise), bring your alibis\nMirrors on the ceiling,\nThe pink champagne on ice\nAnd she said, \'we are all just prisoners here, of our own device\'\nAnd in the master\'s chambers,\nThey gathered for the feast\nThey stab it with their steely knives,\nBut they just can\'t kill the beast\nLast thing I remember, I was\nRunning for the door\nI had to find the passage back to the place I was before\n\'Relax\' said the night man,\n\'We are programmed to receive.\nYou can check out any time you like,\nBut you can never leave!\'\n'
>>> f.readline()
''
>>> f.tell()
1824
>>> len(content)
1778
>>> f.seek(0)
0
>>> f.readline()
'On a dark desert highway, cool wind in my hair\n'
>>> f.readline()
'Warm smell of colitas, rising up through the air\n'
>>> for i in range(5):
	f.readline()

	
'Up ahead in the distance, I saw a shimmering light\n'
'My head grew heavy and my sight grew dim\n'
'I had to stop for the night.\n'
'There she stood in the doorway;\n'
'I heard the mission bell\n'
>>> f.seek(0)
0
>>> content = f.readlines()
>>> type(content)
<class 'list'>
>>> content
['On a dark desert highway, cool wind in my hair\n', 'Warm smell of colitas, rising up through the air\n', 'Up ahead in the distance, I saw a shimmering light\n', 'My head grew heavy and my sight grew dim\n', 'I had to stop for the night.\n', 'There she stood in the doorway;\n', 'I heard the mission bell\n', 'And I was thinking to myself\n', "'This could be heaven or this could be Hell'\n", 'Then she lit up a candle and she showed me the way\n', 'There were voices down the corridor,\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', 'Plenty of room at the Hotel California\n', 'Any time of year (any time of year) you can find it here\n', 'Her mind is Tiffany-twisted, she got the Mercedes bends\n', 'She got a lot of pretty, pretty boys, that she calls friends\n', 'How they dance in the courtyard, sweet summer sweat\n', 'Some dance to remember, some dance to forget\n', 'So I called up the Captain,\n', "'Please bring me my wine'\n", "He said, 'we haven't had that spirit here since nineteen sixty-nine'\n", 'And still those voices are calling from far away,\n', 'Wake you up in the middle of the night\n', 'Just to hear them say"\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', "They livin' it up at the Hotel California\n", 'What a nice surprise (what a nice surprise), bring your alibis\n', 'Mirrors on the ceiling,\n', 'The pink champagne on ice\n', "And she said, 'we are all just prisoners here, of our own device'\n", "And in the master's chambers,\n", 'They gathered for the feast\n', 'They stab it with their steely knives,\n', "But they just can't kill the beast\n", 'Last thing I remember, I was\n', 'Running for the door\n', 'I had to find the passage back to the place I was before\n', "'Relax' said the night man,\n", "'We are programmed to receive.\n", 'You can check out any time you like,\n', "But you can never leave!'\n"]
>>> content[0]
'On a dark desert highway, cool wind in my hair\n'
>>> content[1]
'Warm smell of colitas, rising up through the air\n'
>>> content[2]
'Up ahead in the distance, I saw a shimmering light\n'
>>> content[-1]
"But you can never leave!'\n"
>>> print(content)
['On a dark desert highway, cool wind in my hair\n', 'Warm smell of colitas, rising up through the air\n', 'Up ahead in the distance, I saw a shimmering light\n', 'My head grew heavy and my sight grew dim\n', 'I had to stop for the night.\n', 'There she stood in the doorway;\n', 'I heard the mission bell\n', 'And I was thinking to myself\n', "'This could be heaven or this could be Hell'\n", 'Then she lit up a candle and she showed me the way\n', 'There were voices down the corridor,\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', 'Plenty of room at the Hotel California\n', 'Any time of year (any time of year) you can find it here\n', 'Her mind is Tiffany-twisted, she got the Mercedes bends\n', 'She got a lot of pretty, pretty boys, that she calls friends\n', 'How they dance in the courtyard, sweet summer sweat\n', 'Some dance to remember, some dance to forget\n', 'So I called up the Captain,\n', "'Please bring me my wine'\n", "He said, 'we haven't had that spirit here since nineteen sixty-nine'\n", 'And still those voices are calling from far away,\n', 'Wake you up in the middle of the night\n', 'Just to hear them say"\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', "They livin' it up at the Hotel California\n", 'What a nice surprise (what a nice surprise), bring your alibis\n', 'Mirrors on the ceiling,\n', 'The pink champagne on ice\n', "And she said, 'we are all just prisoners here, of our own device'\n", "And in the master's chambers,\n", 'They gathered for the feast\n', 'They stab it with their steely knives,\n', "But they just can't kill the beast\n", 'Last thing I remember, I was\n', 'Running for the door\n', 'I had to find the passage back to the place I was before\n', "'Relax' said the night man,\n", "'We are programmed to receive.\n", 'You can check out any time you like,\n', "But you can never leave!'\n"]
>>> for line in content:
	print(line)

	
On a dark desert highway, cool wind in my hair

Warm smell of colitas, rising up through the air

Up ahead in the distance, I saw a shimmering light

My head grew heavy and my sight grew dim

I had to stop for the night.

There she stood in the doorway;

I heard the mission bell

And I was thinking to myself

'This could be heaven or this could be Hell'

Then she lit up a candle and she showed me the way

There were voices down the corridor,

I thought I heard them say

Welcome to the Hotel California

Such a lovely place (such a lovely place)

Such a lovely face.

Plenty of room at the Hotel California

Any time of year (any time of year) you can find it here

Her mind is Tiffany-twisted, she got the Mercedes bends

She got a lot of pretty, pretty boys, that she calls friends

How they dance in the courtyard, sweet summer sweat

Some dance to remember, some dance to forget

So I called up the Captain,

'Please bring me my wine'

He said, 'we haven't had that spirit here since nineteen sixty-nine'

And still those voices are calling from far away,

Wake you up in the middle of the night

Just to hear them say"

Welcome to the Hotel California

Such a lovely place (such a lovely place)

Such a lovely face.

They livin' it up at the Hotel California

What a nice surprise (what a nice surprise), bring your alibis

Mirrors on the ceiling,

The pink champagne on ice

And she said, 'we are all just prisoners here, of our own device'

And in the master's chambers,

They gathered for the feast

They stab it with their steely knives,

But they just can't kill the beast

Last thing I remember, I was

Running for the door

I had to find the passage back to the place I was before

'Relax' said the night man,

'We are programmed to receive.

You can check out any time you like,

But you can never leave!'

>>> for line in content:
	if('colitas' in line):
		print(line)

		
Warm smell of colitas, rising up through the air

>>> f.close()
>>> content
['On a dark desert highway, cool wind in my hair\n', 'Warm smell of colitas, rising up through the air\n', 'Up ahead in the distance, I saw a shimmering light\n', 'My head grew heavy and my sight grew dim\n', 'I had to stop for the night.\n', 'There she stood in the doorway;\n', 'I heard the mission bell\n', 'And I was thinking to myself\n', "'This could be heaven or this could be Hell'\n", 'Then she lit up a candle and she showed me the way\n', 'There were voices down the corridor,\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', 'Plenty of room at the Hotel California\n', 'Any time of year (any time of year) you can find it here\n', 'Her mind is Tiffany-twisted, she got the Mercedes bends\n', 'She got a lot of pretty, pretty boys, that she calls friends\n', 'How they dance in the courtyard, sweet summer sweat\n', 'Some dance to remember, some dance to forget\n', 'So I called up the Captain,\n', "'Please bring me my wine'\n", "He said, 'we haven't had that spirit here since nineteen sixty-nine'\n", 'And still those voices are calling from far away,\n', 'Wake you up in the middle of the night\n', 'Just to hear them say"\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face.\n', "They livin' it up at the Hotel California\n", 'What a nice surprise (what a nice surprise), bring your alibis\n', 'Mirrors on the ceiling,\n', 'The pink champagne on ice\n', "And she said, 'we are all just prisoners here, of our own device'\n", "And in the master's chambers,\n", 'They gathered for the feast\n', 'They stab it with their steely knives,\n', "But they just can't kill the beast\n", 'Last thing I remember, I was\n', 'Running for the door\n', 'I had to find the passage back to the place I was before\n', "'Relax' said the night man,\n", "'We are programmed to receive.\n", 'You can check out any time you like,\n', "But you can never leave!'\n"]
>>> f = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\B01\day02\hotel_california2.txt", "w")
>>> f.write('Modified Version \n\n')
19
>>> new_content = []
>>> for line in content:
	new_content.append(line.upper())

	
>>> new_content
['ON A DARK DESERT HIGHWAY, COOL WIND IN MY HAIR\n', 'WARM SMELL OF COLITAS, RISING UP THROUGH THE AIR\n', 'UP AHEAD IN THE DISTANCE, I SAW A SHIMMERING LIGHT\n', 'MY HEAD GREW HEAVY AND MY SIGHT GREW DIM\n', 'I HAD TO STOP FOR THE NIGHT.\n', 'THERE SHE STOOD IN THE DOORWAY;\n', 'I HEARD THE MISSION BELL\n', 'AND I WAS THINKING TO MYSELF\n', "'THIS COULD BE HEAVEN OR THIS COULD BE HELL'\n", 'THEN SHE LIT UP A CANDLE AND SHE SHOWED ME THE WAY\n', 'THERE WERE VOICES DOWN THE CORRIDOR,\n', 'I THOUGHT I HEARD THEM SAY\n', 'WELCOME TO THE HOTEL CALIFORNIA\n', 'SUCH A LOVELY PLACE (SUCH A LOVELY PLACE)\n', 'SUCH A LOVELY FACE.\n', 'PLENTY OF ROOM AT THE HOTEL CALIFORNIA\n', 'ANY TIME OF YEAR (ANY TIME OF YEAR) YOU CAN FIND IT HERE\n', 'HER MIND IS TIFFANY-TWISTED, SHE GOT THE MERCEDES BENDS\n', 'SHE GOT A LOT OF PRETTY, PRETTY BOYS, THAT SHE CALLS FRIENDS\n', 'HOW THEY DANCE IN THE COURTYARD, SWEET SUMMER SWEAT\n', 'SOME DANCE TO REMEMBER, SOME DANCE TO FORGET\n', 'SO I CALLED UP THE CAPTAIN,\n', "'PLEASE BRING ME MY WINE'\n", "HE SAID, 'WE HAVEN'T HAD THAT SPIRIT HERE SINCE NINETEEN SIXTY-NINE'\n", 'AND STILL THOSE VOICES ARE CALLING FROM FAR AWAY,\n', 'WAKE YOU UP IN THE MIDDLE OF THE NIGHT\n', 'JUST TO HEAR THEM SAY"\n', 'WELCOME TO THE HOTEL CALIFORNIA\n', 'SUCH A LOVELY PLACE (SUCH A LOVELY PLACE)\n', 'SUCH A LOVELY FACE.\n', "THEY LIVIN' IT UP AT THE HOTEL CALIFORNIA\n", 'WHAT A NICE SURPRISE (WHAT A NICE SURPRISE), BRING YOUR ALIBIS\n', 'MIRRORS ON THE CEILING,\n', 'THE PINK CHAMPAGNE ON ICE\n', "AND SHE SAID, 'WE ARE ALL JUST PRISONERS HERE, OF OUR OWN DEVICE'\n", "AND IN THE MASTER'S CHAMBERS,\n", 'THEY GATHERED FOR THE FEAST\n', 'THEY STAB IT WITH THEIR STEELY KNIVES,\n', "BUT THEY JUST CAN'T KILL THE BEAST\n", 'LAST THING I REMEMBER, I WAS\n', 'RUNNING FOR THE DOOR\n', 'I HAD TO FIND THE PASSAGE BACK TO THE PLACE I WAS BEFORE\n', "'RELAX' SAID THE NIGHT MAN,\n", "'WE ARE PROGRAMMED TO RECEIVE.\n", 'YOU CAN CHECK OUT ANY TIME YOU LIKE,\n', "BUT YOU CAN NEVER LEAVE!'\n"]
>>> f.writelines(new_content)
>>> f.write('\n\nOriginal by Eagles\n')
21
>>> f.close()
>>> 
