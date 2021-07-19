class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    def item_count(self):
        return len(self.collection)
        
    def page_count(self):
        if self.item_count() and self.item_count() % self.items_per_page:
            return self.item_count() // self.items_per_page + 1
        elif self.item_count():
            return self.item_count() // self.items_per_page
        
        return -1
        
    def page_item_count(self,page_index):
        if page_index in range(0, self.page_count()):
            if (page_index == self.page_count() - 1 
                    and self.item_count() % self.items_per_page):
                return self.item_count() % self.items_per_page
            return self.items_per_page

        return -1
        
    def page_index(self,item_index):
        if (item_index in range(0, self.item_count()) 
                and self.collection 
                and self.items_per_page):
            if item_index <= self.items_per_page:
                return 0
            elif item_index % self.items_per_page:
                return item_index // self.items_per_page
            elif not item_index % self.items_per_page:
                return item_index // self.items_per_page - 1

        return -1
