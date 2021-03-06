from cbpi.api.step import CBPiStep, StepResult
from cbpi.api.dataclasses import Kettle, Props
from cbpi.api import *
import logging
from cbpi.api.config import ConfigType
from cbpi.api.base import CBPiBase
from voluptuous.schema_builder import message
from cbpi.api.dataclasses import NotificationAction, NotificationType


@parameters([Property.Number(label="Targettemp", configurable=True, description="Target temperature for kettle"),
            Property.Kettle(label="Kettle")])
class TargetStep(CBPiStep):

    async def on_start(self):
        try:
            self.kettle = self.get_kettle(self.props.get("Kettle", None))
            self.kettle.target_temp = int(self.props.get("Targettemp", 0))
            #logging.info("TargetTemp Name: {} id: {} TargetTemp: {} ".format(self.kettle.name, self.kettle.id, self.kettle.target_temp))
            await self.set_target_temp(self.kettle.id, self.kettle.target_temp)
        except Exception as e:
            logging.error("Failed to set Target Temp {} {}".format(id, e))

    async def NextStep(self, **kwargs):
        await self.next()

    async def on_stop(self):
        self.summary = ""
        await self.push_update()

    async def run(self):
        self.AutoNext = True
        self.cbpi.notify('Target temperature changed to: ', self.kettle.target_temp, NotificationType.INFO)
        await self.next()

        return StepResult.DONE


def setup(cbpi):
    '''
    This method is called by the server during startup 
    Here you need to register your plugins at the server
    :param cbpi: the cbpi core 
    :return: 
    '''

    cbpi.plugin.register("TargetStep", TargetStep)
