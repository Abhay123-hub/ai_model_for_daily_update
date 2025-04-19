from State import State
from prompts import PromptManager
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Optional
import json
import re
from LLMManager import LLMManager
class Agent:
    def __init__(self):
        self.prompt_manager = PromptManager()
        llm_manager = LLMManager()
        self.llm = llm_manager.get_llm() ## this is the open ai llm
    def Math_Agent(self,state:State):
        "This is a Math specific agent only designed for doing Mathematics related work"
        data = state["input"]
        math_part = data.get("Math")
        ## now i need to check either today the student attended the class or he did the revision
        revision = math_part.get("math_revision",None)
        if revision == None:
            ## means the student has attended the class
            math_revision = "no"
        else:
            math_revision = "yes" ## means today student has done the revision
        return {"math_revision":math_revision,"math_part":math_part}
    def math_router(self,state:State) ->str: ## the router which will decide either i need to go to revision agent or the class agent
        input = state.get("input")
        math = input.get("Math")
        math_revision = math.get("math_revision")
        if math_revision == None:
            return "class_attended"
        else:
            return "class_revision"
    def math_class(self,state:State)->dict:
        """  In this function we will provide the entire data regarding math_class,we will process that data and will make a report for today
        A detialed report.
                """
        ## here we do know that today student has attended the class and we need to provide the data regarding the class
        input = state.get("input")
        math = input.get("Math")
        math_data = math.get("math_class")
        topic_studied = math_data.get("topic_studied","Not Provided")
        understanding_rate = math_data.get("understanding_rate","Not Provided")
        confidence_level = math_data.get("confidence_level","Not Provided")
        difficult_part = math_data.get("difficult_part","Not Provided")
        pace = math_data.get("pace","Not Provided")
        doubts_asked = math_data.get("doubts_asked","Not Provided")
        topic_new = math_data.get("topic_new","Not Provided") ## new  or not new
        quiz_score = math_data.get("quiz_score","Not Provided")
        raw_prompt = self.prompt_manager.get_prompt_for_math_class_agent() ## this is the raw prompt
        prompt = raw_prompt.format(
            topic_studied = topic_studied,
            understanding_rate=understanding_rate,
            confidence_level=confidence_level,
            difficult_part=difficult_part,
            pace=pace,
            doubts_asked=doubts_asked,
            topic_new= topic_new,
            quiz_score=quiz_score,
        )
        messages = [SystemMessage(content=prompt)]
        
        response = self.llm.invoke(messages).content
        return {'math_report_class':str(response)}
    def math_revision(self,state:State)->dict:
        """In this function we will provide the data regarding the student revision day.Here the student will put the data regarding the reviison 
        he did today.Based on the data provided will give a daily report.
        """
        input = state.get("input")
        math = input.get("Math")
        math_data = math.get("math_revision") ## the local variable not the global variable
        topic = math_data.get("topic","Not Provided")
        type = math_data.get("type","Not Provided") ## it is a multi select option like "read theory,watched video" in string only
        questions_solved = math_data.get("solved_questions","Not Provided")
        questions_corrected = math_data.get("questions_corrected","Not Provided")
        time_spent = math_data.get("time_spent","Not Provided")
        confidence_level = math_data.get("confidence_level","Not Provided")
        doubts = math_data.get("doubts","Not Provided") ## doubts or no doubts
        doubt_part = math_data.get("doubt_part","Not Provided")
        helpful = math_data.get("helpful","Not Provided") ## helpful or not helpful
        raw_prompt = self.prompt_manager.get_prompt_for_math_revision_agent()
        
        prompt = raw_prompt.format(
            topic=topic,
            type=type,
            questions_solved=questions_solved,
            questions_corrected=questions_corrected,
            time_spent=time_spent,
            confidence_level=confidence_level,
            doubts=doubts,
            doubt_part=doubt_part,
            helpful=helpful
        )
        messages = [SystemMessage(content=prompt)]
        response = self.llm.invoke(messages).content
        return {"math_report_revision":str(response)}
    
    def Physics_Agent(self,state:State):
        "This is a Physics specific agent only designed for doing Physics related work"
        data = state.get("input")
        physics_part = data.get("Physics")
        ## now i need to check either today the student attended the class or he did the revision
        revision = physics_part.get("physics_revision",None)
        if revision == None:
            ## means the student has attended the class
            physics_revision = "no"
        else:
            physics_revision = "yes" ## means today student has done the revision
        return {"physics_revision":physics_revision,"physics_part":physics_part}
    def physics_router(self,state:State) ->str: ## router which will decide either i need to go to revision agent or class agent
        input = state.get("input")
        physics = input.get("Physics")
        physics_revision = physics.get("physics_revision")
        if physics_revision == None:
            return "class_attended"
        else:
            return "class_revision"
    def physics_class(self,state:State)->dict:
        """  In this function we will provide the entire data regarding math_class,we will process that data and will make a report for today
        A detialed report.
                """
        ## here we do know that today student has attended the class and we need to provide the data regarding the class
        input = state.get("input")
        physics = input.get("Physics")
        physics_data = physics.get("physics_class")
        
        topic_studied = physics_data.get("topic_studied","Not Provided")
        understanding_rate = physics_data.get("understanding_rate","Not Provided")
        confidence_level = physics_data.get("confidence_level","Not Provided")
        difficult_part = physics_data.get("difficult_part","Not Provided")
        pace = physics_data.get("pace","Not Provided")
        doubts_asked = physics_data.get("doubts_asked","Not Provided")
        topic_new = physics_data.get("topic_new","Not Provided") ## new  or not new
        quiz_score = physics_data.get("quiz_score","Not Provided")

        raw_prompt = self.prompt_manager.get_prompt_for_physics_class_agent()
        
        prompt = raw_prompt.format(
            topic_studied = topic_studied,
            understanding_rate=understanding_rate,
            confidence_level=confidence_level,
            difficult_part=difficult_part,
            pace=pace,
            doubts_asked=doubts_asked,
            topic_new= topic_new,
            quiz_score=quiz_score,
        )
        messages = [SystemMessage(content=prompt)]
        
        response = self.llm.invoke(messages).content
        return {'physics_report_class':str(response)}
    def physics_revision(self,state:State)->dict:
        """In this function we will provide the data regarding the student revision day.Here the student will put the data regarding the reviison 
        he did today.Based on the data provided will give a daily report.
        """
        input = state.get("input")
        physics = input.get("Physics")
        physics_data = physics.get("physics_revision")
        topic = physics_data.get("topic","Not Provided")
        type = physics_data.get("type","Not Provided") ## it is a multi select option like "read theory,watched video" in string only
        questions_solved = physics_data.get("solved_questions","Not Provided")
        questions_corrected = physics_data.get("questions_corrected","Not Provided")
        time_spent = physics_data.get("time_spent","Not Provided")
        confidence_level = physics_data.get("confidence_level","Not Provided")
        doubts = physics_data.get("doubts","Not Provided") ## doubts or no doubts
        doubt_part = physics_data.get("doubt_part","Not Provided")
        helpful = physics_data.get("helpful","Not Provided") ## helpful or not helpful
        raw_prompt = self.prompt_manager.get_prompt_for_physics_revision_agent()
        
        prompt = raw_prompt.format(
            topic=topic,
            type=type,
            questions_solved=questions_solved,
            questions_corrected=questions_corrected,
            time_spent=time_spent,
            confidence_level=confidence_level,
            doubts=doubts,
            doubt_part=doubt_part,
            helpful=helpful
        )
        messages = [SystemMessage(content=prompt)]
        response = self.llm.invoke(messages).content
        return {"physics_report_revision":str(response)}
    def Organic_Chemistry_Agent(self,state:State):
        "This is a Organic Chemistry specific agent only designed for doing Organic Chemistry related work"
        data = state.get("input")
        organic_chemistry_part = data.get("Organic_Chemistry")
        ## now i need to check either today the student attended the class or he did the revision
        revision = organic_chemistry_part.get("organic_chemistry_revision",None)
        if revision == None:
            ## means the student has attended the class
            organic_chemistry_revision = "no"
        else:
            organic_chemistry_revision = "yes" ## means today student has done the revision
        return {"organic_chemistry_revision":organic_chemistry_revision,"organic_chemistry_part":organic_chemistry_part}
    def organic_chemistry_router(self,state:State) ->str: ## the router which will decide either i need to go to revision agent or the class agent
        input = state.get("input")
        organic_chemistry = input.get("Organic_Chemistry")
        organic_chemistry_revision = organic_chemistry.get("organic_chemistry_revision")
        if organic_chemistry_revision == None:
            return "class_attended"
        else:
            return "class_revision"
    def organic_chemistry_class(self,state:State)->dict:
        """  In this function we will provide the entire data regarding organic_chemistry_class,we will process that data and will make a report for today
        A detialed report.
                """
        ## here we do know that today student has attended the class and we need to provide the data regarding the class
        input = state.get("input")
        organic_chemistry = input.get("Organic_Chemistry")
        organic_data = organic_chemistry.get("organic_chemistry_class")
        topic_studied = organic_data.get("topic_studied","Not Provided")
        understanding_rate = organic_data.get("understanding_rate","Not Provided")
        confidence_level = organic_data.get("confidence_level","Not Provided")
        difficult_part = organic_data.get("difficult_part","Not Provided")
        pace = organic_data.get("pace","Not Provided")
        doubts_asked = organic_data.get("doubts_asked","Not Provided")
        topic_new = organic_data.get("topic_new","Not Provided") ## new  or not new
        quiz_score = organic_data.get("quiz_score","Not Provided")
        raw_prompt = self.prompt_manager.get_prompt_for_organic_chemistry_class_agent()
        prompt = raw_prompt.format(
            topic_studied = topic_studied,
            understanding_rate=understanding_rate,
            confidence_level=confidence_level,
            difficult_part=difficult_part,
            pace=pace,
            doubts_asked=doubts_asked,
            topic_new= topic_new,
            quiz_score=quiz_score,
        )
        messages = [SystemMessage(content=prompt)]
        
        response = self.llm.invoke(messages).content
        return {'organic_chemistry_report_class':str(response)}
    
    def organic_chemistry_revision(self,state:State)->dict:
        """In this function we will provide the data regarding the student revision day.Here the student will put the data regarding the reviison 
        he did today.Based on the data provided will give a daily report.
        """

        input = state.get("input")
        organic_chemistry = input.get("Organic_Chemistry")
        organic_data = organic_chemistry.get("organic_chemistry_revision")
        topic = organic_data.get("topic","Not Provided")
        type = organic_data.get("type","Not Provided") ## it is a multi select option like "read theory,watched video" in string only
        questions_solved = organic_data.get("solved_questions","Not Provided")
        questions_corrected = organic_data.get("questions_corrected","Not Provided")
        time_spent = organic_data.get("time_spent","Not Provided")
        confidence_level = organic_data.get("confidence_level","Not Provided")
        doubts = organic_data.get("doubts","Not Provided") ## doubts or no doubts
        doubt_part = organic_data.get("doubt_part","Not Provided")
        helpful = organic_data.get("helpful","Not Provided") ## helpful or not helpful
    
        raw_prompt = self.prompt_manager.get_prompt_for_organic_chemistry_revision_agent()
        prompt = raw_prompt.format(
            topic=topic,
            type=type,
            questions_solved=questions_solved,
            questions_corrected=questions_corrected,
            time_spent=time_spent,
            confidence_level=confidence_level,
            doubts=doubts,
            doubt_part=doubt_part,
            helpful=helpful
        )
        messages = [SystemMessage(content=prompt)]
        response = self.llm.invoke(messages).content
        return {"organic_chemistry_report_revision":str(response)}

    def inorganic_Chemistry_Agent(self,state:State):
        "This is a InOrganic Chemistry specific agent only designed for doing InOrganic Chemistry related work"
        data = state.get("input")
        inorganic_chemistry_part = data.get("Inorganic_Chemistry")
        ## now i need to check either today the student attended the class or he did the revision
        revision = inorganic_chemistry_part.get("inoragnic_chemistry_revision",None)
        if revision == None:
            ## means the student has attended the class
            inorganic_chemistry_revision = "no"
        else:
            inorganic_chemistry_revision = "yes" ## means today student has done the revision
        return {"inorganic_chemistry_revision":inorganic_chemistry_revision,"inorganic_chemistry_part":inorganic_chemistry_part}

    def inorganic_chemistry_router(self,state:State) ->str: ## the router which will decide either i need to go to revision agent or the class agent
        input = state.get("input")
        inorganic_chemistry = input.get("Inorganic_Chemistry")
        inorganic_chemistry_revision = inorganic_chemistry.get("inorganic_chemistry_revision")
        if inorganic_chemistry_revision == None:
            return "class_attended"
        else:
            return "class_revision"


    def inorganic_chemistry_class(self,state:State)->dict:
        """  In this function we will provide the entire data regarding inorganic_chemistry_class,we will process that data and will make a report for today
        A detialed report.
                """
        ## here we do know that today student has attended the class and we need to provide the data regarding the class
        input = state.get("input")
        inorganic_chemistry = input.get("Inorganic_Chemistry")
        inorganic_data = inorganic_chemistry.get("inorganic_chemistry_class")
        topic_studied = inorganic_data.get("topic_studied","Not Provided")
        understanding_rate = inorganic_data.get("understanding_rate","Not Provided")
        confidence_level = inorganic_data.get("confidence_level","Not Provided")
        difficult_part = inorganic_data.get("difficult_part","Not Provided")
        pace = inorganic_data.get("pace","Not Provided")
        doubts_asked = inorganic_data.get("doubts_asked","Not Provided")
        topic_new = inorganic_data.get("topic_new","Not Provided") ## new  or not new
        quiz_score = inorganic_data.get("quiz_score","Not Provided")
        raw_prompt = self.prompt_manager.get_prompt_for_inorganic_chemistry_class_agent()
        
        prompt = raw_prompt.format(
            topic_studied = topic_studied,
            understanding_rate=understanding_rate,
            confidence_level=confidence_level,
            difficult_part=difficult_part,
            pace=pace,
            doubts_asked=doubts_asked,
            topic_new= topic_new,
            quiz_score=quiz_score,
        )
        messages = [SystemMessage(content=prompt)]
        
        response = self.llm.invoke(messages).content
        return {'inorganic_chemistry_report_class':str(response)}
    def inorganic_chemistry_revision(self,state:State)->dict:
        """In this function we will provide the data regarding the student revision day.Here the student will put the data regarding the reviison 
        he did today.Based on the data provided will give a daily report.
        """
        input = state.get("input")
        inorganic_chemistry = input.get("Inorganic_Chemistry")
        inorganic_data = inorganic_chemistry.get("inorganic_chemistry_revision")
        topic = inorganic_data.get("topic","Not Provided")
        type = inorganic_data.get("type","Not Provided") ## it is a multi select option like "read theory,watched video" in string only
        questions_solved = inorganic_data.get("solved_questions","Not Provided")
        questions_corrected = inorganic_data.get("questions_corrected","Not Provided")
        time_spent = inorganic_data.get("time_spent","Not Provided")
        confidence_level = inorganic_data.get("confidence_level","Not Provided")
        doubts = inorganic_data.get("doubts","Not Provided") ## doubts or no doubts
        doubt_part = inorganic_data.get("doubt_part","Not Provided")
        helpful = inorganic_data.get("helpful","Not Provided") ## helpful or not helpful
          
        raw_prompt = self.prompt_manager.get_prompt_for_inorganic_chemistry_revision_agent()
        
        prompt =raw_prompt.format(
            topic=topic,
            type=type,
            questions_solved=questions_solved,
            questions_corrected=questions_corrected,
            time_spent=time_spent,
            confidence_level=confidence_level,
            doubts=doubts,
            doubt_part=doubt_part,
            helpful=helpful
        )
        messages = [SystemMessage(content=prompt)]
        response = self.llm.invoke(messages).content
        return {"inorganic_chemistry_report_revision":str(response)}

    def Physical_Chemistry_Agent(self,state:State):
        "This is a Physical Chemistry specific agent only designed for doing InOrganic Chemistry related work"
        data = state.get("input")
        physical_chemistry_part = data.get("Physical_Chemistry")
        ## now i need to check either today the student attended the class or he did the revision
        revision = physical_chemistry_part.get("physical_chemistry_revision",None)
        if revision == None:
            ## means the student has attended the class
            physical_chemistry_revision = "no"
        else:
            physical_chemistry_revision = "yes" ## means today student has done the revision
        return {"physical_chemistry_revision":physical_chemistry_revision,"physical_chemistry_part":physical_chemistry_part}


    def physical_chemistry_router(self,state:State) ->str: ## the router which will decide either i need to go to revision agent or the class agent
        input = state.get("input")
        physical_chemistry = input.get("Physical_Chemistry")
        physical_chemistry_revision = physical_chemistry.get("physical_chemistry_revision")
        if physical_chemistry_revision == None:
            return "class_attended"
        else:
            return "class_revision"


    def physical_chemistry_class(self,state:State)->dict:
        """  In this function we will provide the entire data regarding physical chemistry_class,we will process that data and will make a report for today
        A detialed report.
                """
        ## here we do know that today student has attended the class and we need to provide the data regarding the class
        input = state.get("input")
        physical_chemistry = input.get("Physical_Chemistry")
        physical_data = physical_chemistry.get("physical_chemistry_class")
        topic_studied = physical_data.get("topic_studied","Not Provided")
        understanding_rate = physical_data.get("understanding_rate","Not Provided")
        confidence_level = physical_data.get("confidence_level","Not Provided")
        difficult_part = physical_data.get("difficult_part","Not Provided")
        pace = physical_data.get("pace","Not Provided")
        doubts_asked = physical_data.get("doubts_asked","Not Provided")
        topic_new = physical_data.get("topic_new","Not Provided") ## new  or not new
        quiz_score = physical_data.get("quiz_score","Not Provided")
        raw_prompt = self.prompt_manager.get_prompt_for_physical_chemistry_class_agent()
        
        prompt = raw_prompt.format(
            topic_studied = topic_studied,
            understanding_rate=understanding_rate,
            confidence_level=confidence_level,
            difficult_part=difficult_part,
            pace=pace,
            doubts_asked=doubts_asked,
            topic_new= topic_new,
            quiz_score=quiz_score,
        )
        messages = [SystemMessage(content=prompt)]
        
        response = self.llm.invoke(messages).content
        return {'physical_chemistry_report_class':str(response)}

    def physical_chemistry_revision(self,state:State)->dict:
        """In this function we will provide the data regarding the student revision day.Here the student will put the data regarding the reviison 
        he did today.Based on the data provided will give a daily report.
        """
        input = state.get("input")
        physical_chemistry = input.get("Physical_Chemistry")
        physical_data = physical_chemistry.get("physical_chemistry_revision")
        topic = physical_data.get("topic","Not Provided")
        type = physical_data.get("type","Not Provided") ## it is a multi select option like "read theory,watched video" in string only
        questions_solved = physical_data.get("solved_questions","Not Provided")
        questions_corrected = physical_data.get("questions_corrected","Not Provided")
        time_spent = physical_data.get("time_spent","Not Provided")
        confidence_level = physical_data.get("confidence_level","Not Provided")
        doubts = physical_data.get("doubts","Not Provided") ## doubts or no doubts
        doubt_part = physical_data.get("doubt_part","Not Provided")
        helpful = physical_data.get("helpful","Not Provided") ## helpful or not helpful
        raw_prompt = self.prompt_manager.get_prompt_for_physical_chemistry_revision_agent()
        
        prompt = raw_prompt.format(
            topic=topic,
            type=type,
            questions_solved=questions_solved,
            questions_corrected=questions_corrected,
            time_spent=time_spent,
            confidence_level=confidence_level,
            doubts=doubts,
            doubt_part=doubt_part,
            helpful=helpful
        )
        messages = [SystemMessage(content=prompt)]
        response = self.llm.invoke(messages).content
        return {"physical_chemistry_report_revision":str(response)}
    def final_report(self,state:State)->dict:
        "This will provide the final report based on all the reports of all the three subjects"

        math_report = state.get("math_report_class",None)
        if math_report == None:
            math_report = state.get("math_report_revision","Not Provided") ## if not class then revision

        physics_report = state.get("physics_report_class",None)
        if physics_report == None:
            physics_report = state.get("physics_report_revision","Not Provided")

        organic_chemistry_report = state.get("organic_chemistry_report_class",None)
        if organic_chemistry_report == None:
            organic_chemistry_report = state.get("organic_chemistry_report_revision","Not Provided")

        inorganic_chemistry_report = state.get("inorganic_chemistry_report_class",None)
        if inorganic_chemistry_report == None:
            physical_chemistry_report = state.get("inorganic_chemistry_report_revision","Not Provided")

        physical_chemistry_report = state.get("physical_chemistry_report_class",None)
        if physical_chemistry_report == None:
            physical_chemistry_report = state.get("physical_chemistry_report_revision","Not Provided")
        
        prompt = self.prompt_manager.get_prompt_for_final_report().format(
            math_report = math_report,
            physics_report = physics_report,
            organic_chemistry_report=organic_chemistry_report,
            inorganic_chemistry_report=inorganic_chemistry_report,
            physical_chemistry_report=physical_chemistry_report
        )
        
        messages = [SystemMessage(content=prompt)]
        response = self.llm.invoke(messages)
        output_parser = JsonOutputParser()
        parsed_response = output_parser.parse(response.content)
        final_report = str(parsed_response.get("final_response"))
        final_score = int(parsed_response.get("final_score"))


        return {"final_report":final_report,"final_score":final_score}