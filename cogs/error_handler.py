from discord.ext.commands import Cog, MissingRequiredArgument, CommandInvokeError, MemberNotFound, MissingPermissions


class ErrorHandler(Cog):
    #TODO Refactor code, make it more redable and good looking
    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.reply('Please pass in all requirements :rolling_eyes:.')
        elif isinstance(error, CommandInvokeError):
            if ctx.command.name in ['play']:
                await ctx.reply(f"**Error occurred:** {error}")
        elif isinstance(error, MemberNotFound):
            await ctx.reply("Member not found")
        elif isinstance(error, MissingPermissions):
            if ctx.command.name in ['kick', 'ban', 'warn']:
                await ctx.reply("You don't have the required permissions to run this command.")
            else:
                await ctx.reply("You don't have all the requirements :angry:")


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
