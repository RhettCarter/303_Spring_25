import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor


# part A: sequentially download wikipedia content

# A1: use the wikipedia.search method to return a list of topics related to 'generative artificial intelligence'
topics = wikipedia.search('generative artificial intelligence')

# A2: iterate over the topics returned in #1 above using a for loop
start_time = time.perf_counter()

for topic in topics:
        # assign the page contents to a variable named page using the wikipedia.page method
        # be sure to use auto_suggest=False when using this method
        page = wikipedia.page(topic, auto_suggest=False)

        # assign page title to a variable (using page.title)
        title = page.title

        # retrieve the references for that page (using page.references)
        references = page.references

        # write the references (with each reference on its own line) to a .txt file where the name of the file 
        # is the title of the topic.

        out_filename = title + ".txt"
        with open(out_filename, 'wt', encoding='utf-8') as fileobj:
            for r in references:
                fileobj.write(r + '\n')

# print execution time
end_time = time.perf_counter()
lapsed = end_time - start_time
print(f'part A code ran in {lapsed} seconds')



# part B: Concurrently download wikipedia content
# 1. use the wikipedia.search method to return a list of topics related to 'generative artificial intelligence'
topics = wikipedia.search('generative artificial intelligence')

# 2.  Create a function def wiki_dl_and_save(topic): that:
    # retrieves the wikipedia page for the topic
    # gets the title and the references for the topic
    # creates a .txt file where the name of the file is the title of the topic
    # writes the references to the file created in the preceding step (each reference should be on its own line)

def wiki_dl_and_save(topic):
    page = wikipedia.page(topic, auto_suggest=False) # retrieve the wiki page for topic
    title = page.title # gets title for topic
    references = page.references # gets refs for topic
    out_filename = title + ".txt" # creates a .txt file where the name of the file is the title of the topic
    with open(out_filename,'wt',encoding='utf-8') as fileobj: # writes the references to the file created in the preceding step (each reference should be on its own line)
        for r in references:
            fileobj.write(r + '\n')
        

start_time = time.perf_counter()

# Use the ThreadPoolExecutor from the concurrent.futures library to execute concurrently the function
# defined in step 2.
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics)

# print execution time
end_time = time.perf_counter()
lapsed = end_time - start_time
print(f'part B code ran in {lapsed} seconds')






