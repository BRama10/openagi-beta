import { Draggable } from "@hello-pangea/dnd";

interface AgentContainerProps {
  name: string;
  unique: string;
  index: number;
}

export const AgentContainer: React.FC<AgentContainerProps> = ({
  name,
  unique,
  index,
}) => {
  return (
    <Draggable draggableId={`${index}-${unique}`} index={index}>
      {(provided) => (
        <div
        className='w-full h-fit p-4 rounded-lg drop-shadow-md flex items-center justify-center bg-black border-white border-1 border-dashed'
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          ref={provided.innerRef}
        >
        <p className='text-white text-2xl'>{name}</p>
        </div>
      )}
    </Draggable>
  );
};
