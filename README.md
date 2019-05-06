
# Selenium scrapping!

  - Using Selenium Webdriver and beautiful soup to scrape javascipt rendered page.


### Why use this approach ?
  - Beautiful Soup and URLlib can be used to scrape plain HTML pages.
  - But it cannot be directly used to scrape JavaScript rendered pages.
  - So i need to somehow render the page and scrape the data.
  - So i used Selenium to open the page in FireFox browser and fetch the rendered HTML.


### Structure of the page

```html
<div class="ui segment job_list_card" data-v-5b44ba93="">
    <div class="ui bottom aligned grid" data-v-5b44ba93="">
        <div class="twelve wide computer twelve wide tablet sixteen wide mobile column" data-v-5b44ba93="">
            <h3 class="job_name text-ellipsis" data-v-5b44ba93=""> Magento Developer < /h3>
                    <p data-v-5b44ba93=""> <span data-v-5b44ba93="">
                            Full-time
                            <span class="description-fields-separator" data-v-5b44ba93=""> · </span> </span> <span
                            data-v-5b44ba93="">
                            Hyderabad
                            <span class="description-fields-separator" data-v-5b44ba93=""> · </span> </span> <span
                            data-v-5b44ba93="">
                            2 - 8 Years
                        </span></p>
        </div>
        <div class="four wide right aligned computer tablet only column" data-v-5b44ba93=""><span class="date_posted"
                data-v-5b44ba93="">13 hours ago</span></div>
    </div>
</div>
```

I needed to parse the html by traversing to the child elements of this div

The following Code was used to parse out the results

```python
for job in job_lists:
        for child in job.children:
            child1 = child.children
            name = ""
            tpe = ""
            location = ""
            experience = ""
            tme = ""
            for l, ch in enumerate(child1):
                
                try:
                    if l==0:
                        for i,ch2 in enumerate(ch.children):
                            
                            
                            if i==0 :
                                name = ch2.getText().strip()
                                # print(ch2.getText())
                            elif i==2:
                                for k,ch3 in enumerate(ch2):
                                    if k==0:
                                        tpe = ch3.getText().replace("·", "").strip()
                                        # print(tpe)
                                    elif k==2:
                                        location = ch3.getText().replace("·", "").strip()
                                        # print(location)
                                    if k==4:
                                        experience = ch3.getText().replace("·", "").strip()
                                        # print(experience)
                                    # else:
                                        # print(k, ch3)
                        
                    else: 
                        tme = ch.getText()

                except : 
                    pass
            print("name= "+name,"type= "+tpe, "loca= "+ location,"exp= "+    experience, "time = "+ tme)
            jobs_writer.writerow([name, tpe, location, experience, tme])    
    
```