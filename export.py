def type_to_pl(entity):
    return "type_of({i}, {t}).\n".format(i=entity.id, t=entity.type)

def position_to_pl(position):
    return "position({pos.x}, {pos.y}, {pos.z})".format(pos=position)

def orientation_to_pl(orientation):
    return "orientation({ori.x}, {ori.y}, {ori.z}, {ori.w})".format(ori=orientation)

def pose_to_pl(pose):
    return "pose({pos}, {ori})".format(
            pos=position_to_pl(pose.position),
            ori=orientation_to_pl(pose.orientation))

def pose_of_to_pl(entity):
    return "pose_of({id}, {pose}".format(id=entity.id, pose=pose_to_pl(entity.pos))

def export_type_of(entity, f):
    """Export the entity to file f"""
    f.write(type_to_pl(entity))

def export_types_of(entities, f):
    for ent in entities:
        if not ent.id.startswith("_"):
            export_type_of(ent, f)

def export_pose_of(entity, f):
    f.write(pose_if_to_pl(entity))

def export_poses_of(entities, f):
    for ent in entities:
        if not ent.id.startswith("_"):
            export_pose_of(ent, f)
