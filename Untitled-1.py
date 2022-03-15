elif "news on" in query:
            googlenews=GoogleNews()
            query=query.replace("news on","")
            googlenews.search(query)
            googlenews.clear()
            googlenews.getpage(1)
            result = googlenews.result()
            print(len(result))

            for n in range(len(result)):
                print(n)
                for index in result[n]:
                    print(index, '\n', result[n][index])