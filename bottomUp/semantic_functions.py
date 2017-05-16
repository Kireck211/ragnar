import operator
import socket
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
from pymavlink import mavutil

symbolsTable = {}

class InputToken(object):
	def __init__(self, lexeme, value = None):
		self.lexeme = lexeme
		self.value = value
	
	def __str__(self):
		return self.lexeme

def getValue(identifier):
	return symbolsTable[identifier]

op = {
	'+'	: operator.pos,
	'-' : operator.neg,
	'~' : operator.invert,
	'**' : operator.pow,
	'/' : operator.truediv,
	'%' : operator.mod,
	'*' : operator.mul,
	'<<' : operator.lshift,
	'>>' : operator.rshift,
	'&' : operator.and_,
	'^' : operator.xor,
	'|' : operator.or_,
	'<' : operator.lt,
	'<=' : operator.le,
	'>' : operator.gt,
	'>=' : operator.ge,
	'==' : operator.eq,
	'!=' : operator.ne,
	'!' : operator.not_,
	"+=" : operator.iadd,
	"-=" : operator.isub,
	"*=" : operator.imul,
	"/=" : operator.itruediv,
	"%=" : operator.imod,
	">>=": operator.irshift,
	"<<=": operator.ilshift,
	"&=" : operator.iand,
	"|=" : operator.ior,
	"^=" : operator.ixor,
	"**=" : operator.ipow

}


def semantic2(head, poppedList):
	poppedList[1].lexeme = head
	return poppedList[1]

def semantic3(head, poppedList):
	poppedList[1].lexeme = head
	return poppedList[1]

def semantic4(head, poppedList):
	poppedList[1].lexeme = head
	return poppedList[1]

def semantic9(head, poppedList):
	identifier = getValue(poppedList[2].value)
	operator = poppedList[1].value
	value = poppedList[0].value
	symbolsTable[identifier] = op[operator](identifier, value)
	return InputToken(head, symbolsTable[identifier])

def semantic10(head, poppedList):
	identifier = poppedList[2].value
	value = poppedList[0].value
	symbolsTable[identifier] = value
	return InputToken(head, symbolsTable[identifier]) 

def semantic11(head, poppedList):
	identifier = poppedList[2].value
	value = poppedList[0].value
	symbolsTable[identifier] = value
	return InputToken(head, symbolsTable[identifier])


def semantic22_21_20_19_18_17_16_15_14_13_12(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic23(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic24(head, poppedList):
	operand1 = poppedList[0].value
	operand2 = poppedList[2].value
	return InputToken(head, operand1 or operand2)

def semantic25(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic26(head, poppedList):
	operand1 = poppedList[0].value
	operand2 = poppedList[2].value
	return InputToken(head, operand1 and operand2)

def semantic27(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic28(head, poppedList):
	operator = poppedList[1].lexeme
	operand = poppedList[0].value
	return InputToken(head, op[operator](operand))

def semantic29(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic30(head, poppedList):
	operator = poppedList[1].value # Lo is the lexeme, and the operand is stored in value
	operand1 = poppedList[2].value
	operand2 = poppedList[0].value
	return InputToken(head, op[operator](operand1, operand2))

def semantic31(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic37_36_35_34_33_32(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic38(head, poppedList):
	operator = poppedList[1].lexeme
	operand1 = poppedList[2].value
	operand2 = poppedList[0].value
	return InputToken(head, op[operator](operand1, operand2))

def semantic39(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic40(head, poppedList):
	operator = poppedList[1].lexeme
	operand1 = poppedList[2].value
	operand2 = poppedList[0].value
	return InputToken(head, op[operator](operand1, operand2))

def semantic41(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic42(head, poppedList):
	operator = poppedList[1].lexeme
	operand1 = poppedList[2].value
	operand2 = poppedList[0].value
	return InputToken(head, op[operator](operand1, operand2))

def semantic43(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic44(head, poppedList):
	operator = poppedList[1].lexeme
	number = poppedList[2].value
	shift = poppedList[0].value
	return InputToken(head, op[operator](number, shift))

def semantic45(head, poppedList):
	operator = poppedList[1].lexeme
	number = poppedList[2].value
	shift = poppedList[0].value
	return InputToken(head, op[operator](number, shift))

def semantic46(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic47(head, poppedList):
	sumand1 = poppedList[2].value
	sumand2 = poppedList[0].value
	return InputToken(head, sumand1 + sumand2)

def semantic48(head, poppedList):
	minuend = poppedList[2].value
	substraend = poppedList[0].value
	return InputToken(head, minuend - substraend)

def semantic49(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic50(head, poppedList):
	operator = poppedList[1].lexeme
	factor1 = poppedList[2].value
	factor2 = poppedList[0].value
	return InputToken(head, op[operator](factor1, factor2))

def semantic51(head, poppedList):
	operator = poppedList[1].lexeme
	dividend = poppedList[2].value
	divisor = poppedList[0].value
	return InputToken(head, op[operator](dividend, divisor))

def semantic52(head, poppedList):
	operator = poppedList[1].lexeme
	dividend = poppedList[2].value
	divisor = poppedList[0].value
	return InputToken(head, op[operator](dividend, divisor))

def semantic53(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic54(head, poppedList):
	operator = poppedList[1].lexeme
	base = poppedList[2].value
	exponent = poppedList[0].value
	return InputToken(head, op[operator](base, exponent))

def semantic55(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic56(head, poppedList):    # In this instance poppedList must be [NUMBER,Si]
	number = poppedList[0].value
	lexeme = poppedList[0].lexeme
	result = InputToken(head, number)
	
	for operation in reversed(poppedList[1].value): 
		result.value = op[operation](result.value)
		
	return result

def semantic57(head, poppedList):
	poppedList[0].lexeme = head
	return  poppedList[0]

def semantic58(head, poppedList):
	identifier = poppedList[0].value
	value = symbolsTable[identifier]
	result = InputToken(head, value)

	for operation in reversed(poppedList[1].value): 
		result.value = op[operation](result.value)

	return result

def semantic59(head, poppedList):
	value = poppedList[1].value
	result = InputToken(head, value)

	for operation in reversed(poppedList[3].value): 
		result.value = op[operation](result.value)

	return result

def semantic60(head, poppedList):
	poppedList[1].lexeme = head
	return poppedList[1]

def semantic61(head, poppedList):
	poppedList[1].lexeme = head
	return poppedList[1]

def semantic62(head, poppedList):
	inputStream = ""
	if poppedList[1].value == '':
		inputStream = input()
	else:
		inputStream = input(poppedList[1].value)
	inputStream = castValue(inputStream)
	return InputToken(head, inputStream)

def semantic63(head, poppedList):
	element = poppedList[1].value
	poppedList[0].value.insert(0, element)
	return poppedList[0]

def semantic64(head, poppedList):
	return InputToken(head, [])

def semantic65(head, poppedList):
	element = poppedList[1].value
	poppedList[0].value.insert(0,element)
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic66(head, poppedList):
	return InputToken(head, [])

def semantic67(head, poppedList):
	poppedList[1].value.append("+")
	return poppedList[1]

def semantic68(head, poppedList):
	poppedList[1].value.append("-")
	return poppedList[1]

def semantic69(head, poppedList):
	poppedList[1].value.append("~")
	return poppedList[1]

def semantic70(head, poppedList):	
	return InputToken(head, [])

def semantic71(head,poppedList):
	address_port = poppedList[3].value
	ip_address = address_port[:address_port.index(':')]
	print(ip_address)
	port = address_port[address_port.index(':') + 1:]
	socket.inet_aton(ip_address)
	vehicle = connect(address_port, wait_ready = True)
	height = poppedList[1].value
	arm_and_takeoff(vehicle, height)
	return InputToken(head, vehicle)

def semantic72(head, poppedList):
	elements = []
	elements.append(poppedList[4].value)
	elements.append(poppedList[2].value)
	elements.append(poppedList[0].value)
	return InputToken(head, tuple(elements))

def semantic73(head, poppedList):
	vehicle = symbolsTable[poppedList[3].value]
	coords = poppedList[1].value
	a_location = LocationGlobalRelative(coords[0], coords[1], coords[2])
	vehicle.simple_goto(a_location)
	return InputToken(head, vehicle)

def semantic74(head, poppedList):
	pass

def semantic75(head, poppedList):
	print(poppedList[1].value)
	poppedList[1].lexeme = head
	return poppedList[1]

def semantic76(head, poppedList):
	identifier = poppedList[3].value
	vehicle = symbolsTable[identifier]
	vehicle.mode = VehicleMode("AUTO")
	vehicle.airspeed = poppedList[1].value
	return InputToken(head, vehicle)

def semantic77(head, poppedList):
	identifier = poppedList[3].value
	vehicle = symbolsTable[identifier]
	targets = poppedList[1].value
	attach_pois(targets, vehicle, vehicle.location.global_frame)
	vehicle.commands.next = 0
	vehicle.mode = VehicleMode("AUTO")
	while True:
		next_way_point = vehicle.commands.next
		print("Going to {} poi".format(next_way_point))
		if (len(targets) == next_way_point):
			print("Mission finished")
			break
		time.sleep(2)
	return InputToken(head, vehicle)


def semantic87(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic88(head, poppedList):
	return InputToken(head, '')

def semantic89(head, poppedList):
	vehicle = connect(poppedList[1].value, wait_ready=True)
	return InputToken(head, vehicle)

def semantic90(head, poppedList):
	identifier1 = poppedList[3].value
	identifier2 = poppedList[1].value
	address_port = symbolsTable[identifier1]
	print(address_port)
	ip_address = address_port[:address_port.index(':')]
	print(ip_address)
	port = address_port[address_port.index(':') + 1:]
	socket.inet_aton(ip_address)
	vehicle = connect(address_port, wait_ready = True)
	height = symbolsTable[identifier2]
	arm_and_takeoff(vehicle, height)
	return InputToken(head, vehicle)


semantic_functions = {
	2: semantic2,
	3: semantic3,
	9: semantic9,
	10: semantic10,
	11: semantic11,
	12: semantic22_21_20_19_18_17_16_15_14_13_12,
	13: semantic22_21_20_19_18_17_16_15_14_13_12,
	14: semantic22_21_20_19_18_17_16_15_14_13_12,
	15: semantic22_21_20_19_18_17_16_15_14_13_12,
	16: semantic22_21_20_19_18_17_16_15_14_13_12,
	17: semantic22_21_20_19_18_17_16_15_14_13_12,
	18: semantic22_21_20_19_18_17_16_15_14_13_12,
	19: semantic22_21_20_19_18_17_16_15_14_13_12,
	20: semantic22_21_20_19_18_17_16_15_14_13_12,
	21: semantic22_21_20_19_18_17_16_15_14_13_12,
	22: semantic22_21_20_19_18_17_16_15_14_13_12,
	23: semantic23,
	24: semantic24,
	25: semantic25,
	26: semantic26,
	27: semantic27,
	28: semantic28,
	29: semantic29,
	30: semantic30,
	31: semantic31,
	32: semantic37_36_35_34_33_32,
	33: semantic37_36_35_34_33_32,
	35: semantic37_36_35_34_33_32,
	36: semantic37_36_35_34_33_32,
	37: semantic37_36_35_34_33_32,
	38: semantic38,
	39: semantic39,
	40: semantic40,
	41: semantic41,
	42: semantic42,
	43: semantic43,
	44: semantic44,
	45: semantic45,
	46: semantic46,
	47: semantic47,
	48: semantic48,
	49: semantic49,
	50: semantic50,
	51: semantic51,
	52: semantic52,
	53: semantic53,
	54: semantic54,
	55: semantic55,
	56: semantic56,
	57: semantic57,
	58: semantic58,
	59: semantic59,
	60: semantic60,
	61: semantic61,
	62: semantic62,
	63: semantic63,
	64: semantic64,
	65: semantic65,
	66: semantic66,
	67: semantic67,
	68: semantic68,
	69: semantic69,
	70: semantic70,
	71: semantic71,
	72: semantic72,
	73: semantic73,
	74: semantic74,
	75: semantic75,
	76: semantic76,
	77: semantic77,
	87: semantic87,
	88: semantic88,
	89: semantic89,
	90: semantic90
}

def arm_and_takeoff(vehicle, height):
	while not vehicle.is_armable:
		print("Waiting for vehicle to initialise ...")
		time.sleep(2)

	print("Arming motors")
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True

	while not vehicle.armed:
		print("Wainting to arm ...")
		time.sleep(2)

	print("Taking off")
	vehicle.simple_takeoff(height+1)
	while True:
		print("Altitude: ", vehicle.location.global_relative_frame.alt)
		if  vehicle.location.global_relative_frame.alt >= height * 0.95 :
			print("Reached altitude")
			break
		time.sleep(1)

def castValue(inputStream):
	inputStreamTemp = inputStream
	try:
		inputStreamTemp = int(inputStream)
		return inputStreamTemp
	except ValueError:
		try:
			inputStreamTemp = float(inputStream)
			return inputStreamTemp
		except ValueError:
			return inputStream

def attach_pois(targets, vehicle, actual_location):
	cmds = vehicle.commands
	cmds.clear()
	cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, 10))
	if (isinstance(targets, list)):
		for target in targets:
			cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, target[0], target[1], target[2]))
	else:
		cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, target[0], target[1], targets[2]))
	cmds.upload()