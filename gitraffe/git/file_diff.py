from output import getoutput_lines
from log import save_log

def remove_html(line):
    new = line.replace('<', '&lt;')
    new = new.replace('>', '&gt;')
    return new

def get_file_changes(flag, path ,commit, comparsion=None):
    try:
        out = '<pre>'
        if flag == 'M' or flag == 'MM':
            command = 'git diff %s:%s %s:%s' % (comparsion, path, commit, path)
            output = getoutput_lines(command)
            save_log(command, output[0])
            for line in output[1][4:]:
                line = remove_html(line)
                if len(line) > 0:
                    if line[0]=='-':
                        line = '<font color="RED"> %s</font>' % (line)
                    elif line[0]=='+':
                        line = '<font color="GREEN"> %s</font>' % (line)
                    out += line + '\n'
            out += '</pre>'
            return out
        elif flag=='A':
            command = 'git show %s:%s' % (commit, path)
            output = getoutput_lines(command)
            save_log(command, output[0])
            for line in output[1]:
                line = remove_html(line)
                line = '<font color="GREEN"> + %s </font>' % (line)
                out += line + '\n'
            out += '</pre>'
            return out
        elif flag=='D':
            command = 'git show %s:%s' % (comparsion, path)
            output = getoutput_lines(command)
            save_log(command, output[0])
            for line in output[1]:
                line = remove_html(line)
                line = '<font color="RED"> - %s </font>' % (line)
                out += line + '\n'
            out += '</pre>'
            return out
    except UnicodeDecodeError:
        return "Cannot decode this file"