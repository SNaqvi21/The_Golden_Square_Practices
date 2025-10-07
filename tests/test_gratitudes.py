from lib.gratitudes import Gratitudes

# test initial state of gratitude list
def test_state_of_gratitudes():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

# test add() method to ensure it appends gratitude
def test_check_add_method_of_gratitude_class():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("health")
    assert gratitudes.format() == "Be grateful for: family, health"

# test the format() output
def test_format_method_of_gratitude_class():
    gratitudes = Gratitudes()
    gratitudes.add("love")
    gratitudes.add("home")
    gratitudes.add("family")
    gratitudes.add("health")
    assert gratitudes.format() == "Be grateful for: love, home, family, health"


"""
test an empty string
"""
def test_empty_string_of_gratitude_class():
    gratitudes = Gratitudes()
    gratitudes.add("")
    assert gratitudes.format() == "Be grateful for: "

"""
test whitespace
"""
def test_whitespace_input_of_gratitude_class():
    gratitudes = Gratitudes()
    gratitudes.add("    ")
    assert gratitudes.format() == "Be grateful for:     "

"""
test different instances
"""
def test_multiple_instances_of_gratitude_class():
    gratitudes = Gratitudes()
    gratitudes_2 = Gratitudes()
    gratitudes_3 = Gratitudes()
    gratitudes.add("health")
    gratitudes_2.add("family")
    gratitudes_3.add("home")
    assert gratitudes.format() == "Be grateful for: health"
    assert gratitudes_2.format() == "Be grateful for: family"
    assert gratitudes_3.format() == "Be grateful for: home"

    

"""
test an empty string
"""