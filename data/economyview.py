import nextcord
from nextcord.ext import commands


# 
class Confirm(nextcord.ui.View):
"""A discord view prompting 2 buttons asking to confirm or cancel"""
    def __init__(self):
        super().__init__()
        self.value = None

    # 
    @nextcord.ui.button(label='Confirm', style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        self.stop()
    #
    @nextcord.ui.button(label='Cancel', style=nextcord.ButtonStyle.grey)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()
        
    
async def ask(ctx, question =:"Confirm or Cancel"):
    """Sends the view to channel and returns True if confirmed or False if canceled or timed out"""
    self.question = question
    view = Confirm()
    await ctx.send(self.question, view=view)
#Wait for the View to stop listening for input...
    await view.wait()
	    if view.value is None:
	        print('Timed out...')
	        return False
	    elif view.value:
	        print('Confirmed...')
	        return True
	    else:
	        print('Cancelled...')
	        return False

