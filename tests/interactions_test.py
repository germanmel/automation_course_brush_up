from pages.interactions_page import SortablePage, SelectablePage
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
import pytest

class TestInteractions:

    class TestSortablePage:
        locators = SortablePageLocators

        test_data = {
            "list": {
                "tab": locators.TAB_LIST,
                "items": locators.LIST_ITEMS,
                "expected_list": ['Two', 'Three', 'Four', 'Five', 'Six', 'One']
            },
            "grid": {
                "tab": locators.TAB_GRID,
                "items": locators.GRID_ITEMS,
                "expected_list": ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'One']
            }
        }

        @pytest.mark.parametrize("data", test_data.values(), ids=test_data.keys())
        def test_sortable_random(self, driver, data):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_random_item_order(data["tab"], data["items"])
            assert order_before != order_after, \
                f'Order before: {order_before} and order after: {order_after} are equal, but difference was expected'

        @pytest.mark.parametrize("data", test_data.values(), ids=test_data.keys())
        def test_sortable_one_to_end(self, driver, data):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_after = sortable_page.move_one_to_end(data["tab"], data["items"])
            assert order_after == data["expected_list"], \
                f"Unexpected order of items {order_after}"

    class TestSelectablePage:
        locators = SelectablePageLocators()

        test_data = {
            "list": {
                "tab": locators.TAB_LIST,
                "items": locators.LIST_ITEMS,
                "selected": locators.ACTIVE_LIST_ITEMS
            },
            "grid": {
                "tab": locators.TAB_GRID,
                "items": locators.GRID_ITEMS,
                "selected": locators.ACTIVE_LIST_GRID
            }
        }

        @pytest.mark.parametrize("data", test_data.values(), ids=test_data.keys())
        def test_selectable_random(self,driver, data):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            items_for_select, selected_items = selectable_page.select_random_items(data["tab"], data["items"],
                                                                                   data["selected"])
            """Создаём неупорядоченные множества на основе списков"""
            items = set(items_for_select)
            selected = set(selected_items)
            """Сравниваем, 2 множества равны, если содержат одинаковые элементы"""
            assert items == selected, f"Clicked items: {items} and selected items {selected} are different"