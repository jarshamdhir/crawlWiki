import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="Mango"
)
page = wiki_wiki.page("Benjamin F. McAdoo")
if page.exists():
    print(f"text:{page.text}")
    # print(f'Tables: {page.tables}')