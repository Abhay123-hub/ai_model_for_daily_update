from langgraph.graph import END, StateGraph, START
from Agent import Agent
from State import State

class workflow:
    def __init__(self):
        self.agent = Agent()
    
    def create_worklfow(self):
        workflow = StateGraph(State)
        workflow.add_node("Math_Agent",self.agent.Math_Agent)
        workflow.add_node("Math_Class",self.agent.math_class)
        workflow.add_node("Math_Revision",self.agent.math_revision)
        workflow.add_node("Physics_Agent",self.agent.Physics_Agent)
        workflow.add_node("Physics_Class",self.agent.physics_class)
        workflow.add_node("Physics_Revision",self.agent.physics_revision)
        workflow.add_node("Organic_Chemistry_Agent",self.agent.Organic_Chemistry_Agent)
        workflow.add_node("Organic_Chemistry_Class",self.agent.organic_chemistry_class)
        workflow.add_node("Organic_Chemistry_Revision",self.agent.organic_chemistry_revision)
        workflow.add_node("Inorganic_Chemistry_Agent",self.agent.inorganic_Chemistry_Agent)
        workflow.add_node("Inorganic_Chemistry_Class",self.agent.inorganic_chemistry_class)
        workflow.add_node("Inorganic_Chemistry_Revision",self.agent.inorganic_chemistry_revision)
        workflow.add_node("Physical_Chemistry_Agent",self.agent.Physical_Chemistry_Agent)
        workflow.add_node("Physical_Chemistry_Class",self.agent.physical_chemistry_class)
        workflow.add_node("Physical_Chemistry_Revision",self.agent.physical_chemistry_revision)
        workflow.add_node("Final_Report",self.agent.final_report)
        ## defined all the nodes
        ## now joining all the nodes
        workflow.add_edge(START,"Math_Agent")
        workflow.add_edge(START,"Physics_Agent")
        workflow.add_edge(START,"Organic_Chemistry_Agent")
        workflow.add_edge(START,"Inorganic_Chemistry_Agent")
        workflow.add_edge(START,"Physical_Chemistry_Agent")

        workflow.add_conditional_edges("Math_Agent",self.agent.math_router,{"class_attended":"Math_Class","class_revision":"Math_Revision"})
        workflow.add_conditional_edges("Physics_Agent",self.agent.physics_router,{"class_attended":"Physics_Class","class_revision":"Physics_Revision"})
        workflow.add_conditional_edges("Organic_Chemistry_Agent",self.agent.organic_chemistry_router,{"class_attended":"Organic_Chemistry_Class","class_revision":"Organic_Chemistry_Revision"})
        workflow.add_conditional_edges("Inorganic_Chemistry_Agent",self.agent.inorganic_chemistry_router,{"class_attended":"Inorganic_Chemistry_Class","class_revision":"Inorganic_Chemistry_Revision"})
        workflow.add_conditional_edges("Physical_Chemistry_Agent",self.agent.physical_chemistry_router,{"class_attended":"Physical_Chemistry_Class","class_revision":"Physical_Chemistry_Revision"})

        workflow.add_edge("Math_Class","Final_Report")
        workflow.add_edge("Math_Revision","Final_Report")

        workflow.add_edge("Physics_Class","Final_Report")
        workflow.add_edge("Physics_Revision","Final_Report")

        workflow.add_edge("Organic_Chemistry_Class","Final_Report")
        workflow.add_edge("Organic_Chemistry_Revision","Final_Report")

        workflow.add_edge("Inorganic_Chemistry_Class","Final_Report")
        workflow.add_edge("Inorganic_Chemistry_Revision","Final_Report")

        workflow.add_edge("Physical_Chemistry_Class","Final_Report")
        workflow.add_edge("Physical_Chemistry_Revision","Final_Report")

        workflow.add_edge("Final_Report",END)
        app = workflow.compile()
        return app
    
    def execute(self,input_dict):
        app = self.create_worklfow()
        inputs = {"input":input_dict}
        try:
            response = app.invoke(inputs)
            return response
        except Exception as e:
            raise e
            
        
