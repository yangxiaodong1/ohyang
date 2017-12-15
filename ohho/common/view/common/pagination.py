class Pagination(object):
    def __init__(self, total_page, current_page=1, data_count_per_page=10, page_count_per_page=10):
        self.total_page = total_page
        self.current_page = current_page
        self.data_count_per_page = data_count_per_page
        self.page_count_per_page = page_count_per_page

    def get_page_list_of_this_page(self):
        start_page = self.current_page // 10 * 10 + 1
        previous = start_page - 1
        end_page = start_page + self.page_count_per_page
        if end_page > self.total_page:
            next = 0
            end_page = self.total_page + 1
        else:
            next = end_page
        if start_page == end_page:
            end_page = start_page + 1
        return range(start_page, end_page), previous, next
