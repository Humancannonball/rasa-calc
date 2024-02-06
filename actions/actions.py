from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
import operator

class ActionCalculate(Action):
    def name(self) -> Text:
        return "action_calculate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the slot values and convert to float
        try:
            first_number = float(tracker.get_slot('first_number'))
            second_number = float(tracker.get_slot('second_number'))
            operator_str = tracker.get_slot('operator')
        except ValueError:
            dispatcher.utter_message(text="I'm sorry, I didn't understand the numbers.")
            return []

        # Map the operator string to a function
        ops = {
            "add": operator.add,
            "subtract": operator.sub,
            "multiply": operator.mul,
            "divide": operator.truediv
        }
        op_func = ops.get(operator_str)

        # Perform the calculation and respond with the result
        if op_func:
            try:
                result = op_func(first_number, second_number)
                dispatcher.utter_message(text=f"The result is {result}")
            except ZeroDivisionError:
                dispatcher.utter_message(text="Sorry, I cannot divide by zero.")
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't understand the operation.")

        return []