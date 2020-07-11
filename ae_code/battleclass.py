import openpyxl
import random

class battleRole(object):
	"""docstring for battleRole"""
	def __init__(self,camp,role_id,name,hp,sp,atk,continue_atk,armor,hit,eva,cri,atk_spd,atk_dis,maxhp,skill_pool):
		super(battleRole, self).__init__()
		self.camp           = camp
		self.role_id        = role_id
		self.name           = name
		self.hp             = hp
		self.sp             = sp
		self.atk            = atk
		self.continue_atk   = continue_atk
		self.armor          = armor
		self.hit            = hit
		self.eva            = eva
		self.cri            = cri
		self.atk_spd        = atk_spd
		self.atk_dis        = atk_dis
		self.maxhp          = maxhp
		self.skill_pool     = skill_pool
	def add_skill(self,skill_id):
		if skill_id not in self.skill_pool:
			self.skill_pool.append(skill_id)
		else:
			print("{}已经拥有这个技能啦".format(self.name,skill_id))
	def returnArmor(self):
		return self.armor



class RoleSkill(object):
	"""docstring for RoleSkill"""
	def __init__(self, skill_id,func,funcParam1,funcParam2,funcParam3,desc):
		super(RoleSkill, self).__init__()
		self.skillId       = skillId,
		self.func          = func
		self.funcParam1    = funcParam1
		self.funcParam2	   = funcParam2
		self.funcParam3	   = funcParam3
		self.desc          = desc

class BattleFunc(object):
	"""docstring for BattleFunc"""
	def __init__(self,funcId,funcType,funcParam1,funcParam2,funcParam3):
		# super(battleRole, self).__init__()
		# super().__init__()
		# super(BattleFunc, self).__init__()# battleRole.__init__(self,1,1,"道具达人",50,50,6,0,5,1,0.25,0.1,1,1,50,[1])
		self.funcId        = funcId
		self.funcType      = funcType
		self.funcParam1    = funcParam1
		self.funcParam2	   = funcParam2
		self.funcParam3	   = funcParam3

	def cause_damage(self):
		damage     = self.funcParam1/10000 * self.funcParam2
		print("百分比{0}，属性伤害：{1}".format(self.funcParam1/10000,self.funcParam2))
		return damage


	def cause_damage_and_vertigo(self):
		damage     = self.funcParam1 
		vertigo_round = self.funcParam2
		return [damage,vertigo_round]

	def invincible_and_cause_damage(self):
		damage = self.funcParam1
		invincible_round = self.funcParam2


Role  = battleRole(1,1,"道具达人",50,50,6,0,5,1,0.25,0.1,1,1,50,[1])
Func1 = BattleFunc(1,1,50000,500,0)
print(Func1.funcParam1)
print(Role.armor)
print(Func1.armor_damage())
# print(damage)
