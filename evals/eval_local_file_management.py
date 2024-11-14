import arcade_local_file_management
from arcade_local_file_management.tools.hello import say_hello

from arcade.sdk import ToolCatalog
from arcade.sdk.eval import (
    EvalRubric,
    EvalSuite,
    SimilarityCritic,
    tool_eval,
)

# Evaluation rubric
rubric = EvalRubric(
    fail_threshold=0.85,
    warn_threshold=0.95,
)


catalog = ToolCatalog()
catalog.add_module(arcade_local_file_management)


@tool_eval()
def local_file_management_eval_suite():
    suite = EvalSuite(
        name="local_file_management Tools Evaluation",
        system_message="You are an AI assistant with access to local_file_management tools. Use them to help the user with their tasks.",
        catalog=catalog,
        rubric=rubric,
    )

    suite.add_case(
        name="Saying hello",
        user_message="He's actually right here, say hi to him!",
        expected_tool_calls=[
            (
                say_hello,
                {
                    "name": "John Doe"
                }
            )
        ],
        rubric=rubric,
        critics=[
            SimilarityCritic(critic_field="name", weight=0.5),
        ],
        additional_messages=[
            { "role": "user", "content": "My friend's name is John Doe." },
            { "role": "assistant", "content": "It is great that you have a friend named John Doe!" },
        ]
    )

    return suite