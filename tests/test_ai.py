import pytest
from ai import recreate_recipe_ai_bot

def test_recreate_recipe_ai_bot(mocker):
    test_food = {
        'food_name': 'Big Mac',
        'food_restaurant': "McDonald's",
        'food_category': "Burgers"
    }

    mock_response = mocker.Mock()
    mock_response.choices = [
        mocker.Mock(message=mocker.Mock(content='### Ingredients\n Secret Sauce\n Beef'))
    ]

    mocker.patch("ai.client.chat.completions.create", return_value=mock_response)

    result = recreate_recipe_ai_bot(test_food)

    assert "Secret Sauce" in result
    assert "### Ingredients" in result