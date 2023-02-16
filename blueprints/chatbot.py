from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import QuestionForm, AnswerForm, ChatbotQuestionForm
from models import QuestionModel, AnswerModel
from exts import db
from decorators import login_required
import openai
from config import MY_CHATBOT_API_KEY

bp = Blueprint("chatbot", __name__, url_prefix="/chatbot")

openai.api_key = "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"


@bp.route("/")
def chatbot():
    return render_template("chatbot.html", answer="")


@bp.route("/get_answer/<answer>")
def get_answer(answer):
    result = answer
    return render_template("chatbot.html", answer=result)


@bp.route("/get_response", methods=["POST", "GET"])
def get_response():
    # form = ChatbotQuestionForm(request.form)
    prompt = request.form.get("question")
    print(prompt)
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=4000
    )
    print(response)
    ai_answer = response.choices[0].text
    return redirect(url_for("chatbot.get_answer", answer=ai_answer))
